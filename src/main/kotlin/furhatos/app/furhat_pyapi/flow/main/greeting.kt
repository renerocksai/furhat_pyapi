package furhatos.app.furhat_pyapi.flow.main

import furhatos.app.furhat_pyapi.flow.Parent
import furhatos.flow.kotlin.*
import furhatos.nlu.common.No
import furhatos.nlu.common.Yes

val Greeting : State = state(Parent) {
    onEntry {
        // furhat.ask("Should I say Hello World?")
    }

    onResponse<Yes> {
        furhat.say("Hello World! .")
    }

    onButton("python") {
        var response = khttp.get("http://localhost:5000/greet/rene");
        var greeting = response.jsonObject.get("greeting");
        print(greeting);
        furhat.say(greeting as String);
    }

    onResponse<No> {
        furhat.say("Ok.")
    }
}
