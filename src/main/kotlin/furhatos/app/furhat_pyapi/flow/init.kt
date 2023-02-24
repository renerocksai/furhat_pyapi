package furhatos.app.furhat_pyapi.flow

import furhatos.app.furhat_pyapi.flow.main.Idle
import furhatos.app.furhat_pyapi.setting.distanceToEngage
import furhatos.app.furhat_pyapi.setting.maxNumberOfUsers
import furhatos.flow.kotlin.*
import furhatos.flow.kotlin.voice.Voice

val Init : State = state() {
    init {
        /** Set our default interaction parameters */
        users.setSimpleEngagementPolicy(distanceToEngage, maxNumberOfUsers)
        furhat.voice = Voice("Matthew")
        /** start the interaction */
        goto(Idle)
    }
}
