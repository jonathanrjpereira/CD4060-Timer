# CD4060 Timer

The timer can be set for a time delay from 15 seconds upto 24 hours.
The time delay can be easily changed to control the state of any device connected to the output.

**Order PCB:**

## Electronic Components
| Qty | Component | Buy |
| ------------- | ------------- | ------------- |
| 1 | 555 |[AliExpress](http://s.click.aliexpress.com/e/sCv1ACC) |
| 2 | 3KΩ Resistor |[AliExpress](http://s.click.aliexpress.com/e/bh4eqrQs) |
| 4 | 10KΩ Resistor |[AliExpress](http://s.click.aliexpress.com/e/bh4eqrQs) |
| 1 | 1MΩ Potentiometer |[AliExpress](http://s.click.aliexpress.com/e/bR23nRuG) |
| 1 | IN4004 Diode |[AliExpress](http://s.click.aliexpress.com/e/HW1fm16) |
| 2 | Tactile Momentary Push Buttons |[AliExpress](http://s.click.aliexpress.com/e/c77Ajrpq) |
| 2 | 5mm LED |[AliExpress](http://s.click.aliexpress.com/e/wuFpLXS) |
| 2 | 100uF Capacitor |[AliExpress](http://s.click.aliexpress.com/e/c9FHzl5W) |
| 2 | 0.1uF (100nF) Capacitor |[AliExpress](http://s.click.aliexpress.com/e/byQG0DZW) |
| 1 | 2 Pin Screw Terminal |[AliExpress](http://s.click.aliexpress.com/e/bj5UNUs0) |
| 1 | 3 Pin Screw Terminal |[AliExpress](http://s.click.aliexpress.com/e/bj5UNUs0) |
| 1 | Relay |[AliExpress](http://s.click.aliexpress.com/e/xyrHlu8) |
| 1 | 12VDC Adapter |[AliExpress](http://s.click.aliexpress.com/e/V0x0bms) |
| 1 | SPDT Slide Switch |[AliExpress](http://s.click.aliexpress.com/e/cDjWUvjK) |
| 1 | PCB |[AliExpress](http://s.click.aliexpress.com/e/dhgwzKY) |


| Tools | Buy |
|--|--|
|Soldering Iron|[AliExpress](http://s.click.aliexpress.com/e/E83bSJI) |
|Soldering Wire|[AliExpress](http://s.click.aliexpress.com/e/PdhB0nm) |
|Mini PCB Hand Drill + Bits|[AliExpress](http://s.click.aliexpress.com/e/b93tomjI) |

## Working
**CD4060:**

The CD4060 consists of an oscillator section and 14 ripple carry binary counter stages. The oscillator configuration allows design of RC oscillator circuits. A RESET input is provided which resets the counter to the all-0's state and disables the oscillator. The counters are reset to the zero state by a logical “1” at the reset input independent of clock. The counters are advanced one count on the negative transition of each clock pulse.

![Pinout](https://github.com/jonathanrjpereira/555-Timer-1sec-to-100sec/blob/master/img/pinout.png)
![Pin Description](https://github.com/jonathanrjpereira/555-Timer-1sec-to-100sec/blob/master/img/pindescription.png)

**Timing Cycle:**

![](https://latex.codecogs.com/png.latex?%5Clarge%20Time%20%3D%20t%20%3D%20%5Cfrac%7B2%5E%7Bn%7D%7D%7Bf_%7Bosc%7D%7D)

where n is the Output Number i.e. ![](https://latex.codecogs.com/png.latex?%5Clarge%20Q_%7Bn%7D)



**Circuit:**

![Monostable Waveform](https://github.com/jonathanrjpereira/555-Timer-1sec-to-100sec/blob/master/img/wave.png)

The figure above shows the waveforms generated in this mode of operation. Since the charge and the threshold level of the comparator are both directly proportional to supply voltage, the timing interval is independent of supply.

![Block Diagram](https://github.com/jonathanrjpereira/555-Timer-1sec-to-100sec/blob/master/img/BD.png)

Separate input triggers are used to start and reset the timer. The RC network determines the period of the output pulse. High power appliances can be controlled through a relay acting as a switch.

![Schematic](https://github.com/jonathanrjpereira/555-Timer-1sec-to-100sec/blob/master/img/sch.png)

The LM555 has a maximum typical supply voltage rating of 16V while the relay's armature coil is enabled at 12V. Hence a 12V power supply is used to minimize the number of components such as linear voltage regulators. When pin 2 of the LM555 is triggered (by shorting it to ground) through the momentary switch S1, the timer is started.

The timer generates an output pulse with an ON time period determined by the RC network i.e t = 1.1RC . In this case the fixed value of the capacitor is 100uF. The value of R consists of a 10KΩ resistor in series with a 1MΩ potentiometer. We can vary the potentiometer to change the time period of the output pulse.

For example, if the potentiometer is set to 0Ω, the value of R is equal to 10KΩ.
Hence t = 1.1 x 10K x 100u = 1 second.

But if the pot is set to 1MΩ, the value of R is equal to 1MΩ + 10KΩ = 1010KΩ.
Hence t = 1.1 x 1010K x 100u = 100 seconds.

When pin 4 of the LM555 is triggered (by shorting it to ground) through the momentary switch S2, the timer is reset.

When the timer starts, the relay turns ON. Hence the Common(COM) terminal of the relay is shorted to the Normally Open (NO) terminal. A high power load can be connected to this terminal such as a light bulb or water pump. A transistor Q1 acts as a switch an ensures sufficient drive current is provided to the relay. Diode D1 acts as a flyback diode which protects the transistor Q1 from voltage spikes caused by the relay coil.

LED2 turns on in order to indicate when the relay is turned ON. LED1 indicates the circuit is powered ON. An SPDT switch S3 is used to switch the circuit ON. Capacitors C2 and C4 are used to filter noise in the supply line.


## Contributing🛠
Are you an engineer or hobbyist who has a great idea for a new feature in this project? Maybe you have a good idea for a bug fix? Feel free to grab our code & schematics from Github and tinker with it. Don't forget to smash ⭐️ & the Pull Request button.

[![alt text][1.1]][1] [![alt text][2.1]][2] [![alt text][3.1]][3]

[1.1]: https://github.com/jonathanrjpereira/Social-Media-README/blob/master/youtube.png (YouTube)
[2.1]: https://github.com/jonathanrjpereira/Social-Media-README/blob/master/instagram.png (Instagram)
[3.1]: https://github.com/jonathanrjpereira/Social-Media-README/blob/master/github.png (GitHub)

[1]: https://www.youtube.com/channel/UCRW-41O1vy98KKgJRQoYzdg
[2]: https://www.instagram.com/electroguruji/
[3]: https://github.com/jonathanrjpereira
