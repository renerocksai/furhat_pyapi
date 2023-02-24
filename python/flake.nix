{
  description = "python flask api";
  # nixConfig.bash-prompt = "nix-develop $ ";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/release-22.11";
    flake-utils.url = "github:numtide/flake-utils";

    unstable.url = "github:nixos/nixpkgs/nixpkgs-unstable";
    
    # required for latest neovim
    neovim-flake.url = "github:neovim/neovim?dir=contrib";

    # this is how to point nvim to a specific commit:
    # 1. go to github:nixos-community/nvim-nightly 
    # 2. check where the build doesn't fail 
    # 3. check out the neovim revision in the diff output of flake.lock
    # neovim-flake.url = "github:neovim/neovim/08ebf8d3a80c65b01d493ca84ad2ab7304a669f9?dir=contrib";
    neovim-flake.inputs.nixpkgs.follows = "nixpkgs";

    # Used for shell.nix
    flake-compat = {
      url = github:edolstra/flake-compat;
      flake = false;
    };
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
    ...
  } @ inputs: let
    overlays = [
      # Other overlays
      (final: prev: {
        neovim-nightly-pkgs = inputs.neovim-flake.packages.${prev.system};
      })
    ];
  in
    flake-utils.lib.eachDefaultSystem (
      system: let
        pkgs = import nixpkgs {inherit overlays system; };
      in rec {
        devShells.default = pkgs.mkShell {
          nativeBuildInputs = with pkgs; [
            neovim-nightly-pkgs.neovim
            bat
            wrk
            python39
            python39Packages.flask
            python39Packages.flask-restful
            python39Packages.gunicorn
          ];

          buildInputs = with pkgs; [
            # we need a version of bash capable of being interactive
            # as opposed to a bash just used for building this flake 
            # in non-interactive mode
            bashInteractive 
          ];

          shellHook = ''
            # once we set SHELL to point to the interactive bash, neovim will 
            # launch the correct $SHELL in its :terminal 
            export SHELL=${pkgs.bashInteractive}/bin/bash
          '';

        };


        # For compatibility with older versions of the `nix` binary
        devShell = self.devShells.${system}.default;
      }
    );
}
