.PHONY: all

all:
	./gradlew shadowJar
	echo "built skill in ./build/libs"

