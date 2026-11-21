# 04 · Nobody can hear the meeting-room presenter

**Fictional onsite incident · One presenter · Meeting starts in five minutes.** Alex can hear the call through the dock. Remote participants hear silence from the room.

| Check while Alex speaks | Simulated result |
| --- | --- |
| Windows input meter for the USB speakerphone | Moves with speech. |
| Microphone selected in Teams | Laptop microphone, although the laptop lid is closed. |
| Far-end listener | Hears no speech. |

**L1 decision.** Select the USB speakerphone as the Teams microphone, then make a short call with a colleague. A moving Windows meter confirms a local signal. The remote listener establishes whether it reaches the call.

**Employee update.** “Windows can hear the room microphone. Teams is using the laptop microphone. I’ll switch it over and ask a colleague to listen before your meeting.”

**Closure or handoff.** Close only after the listener confirms clear speech with the intended room setup and Alex agrees. If the Windows meter also stays flat, check physical mute, input selection and the dock connection. If the meter works and Teams already uses the correct input, hand endpoint support the device name, client version and call time. [Input record](audio.json) · [Employee guide](../docs/microphone-en.md)
