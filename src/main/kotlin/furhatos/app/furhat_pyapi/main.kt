package furhatos.app.furhat_pyapi

import furhatos.app.furhat_pyapi.flow.*
import furhatos.skills.Skill
import furhatos.flow.kotlin.*

class Furhat_pyapiSkill : Skill() {
    override fun start() {
        Flow().run(Init)
    }
}

fun main(args: Array<String>) {
    Skill.main(args)
}
