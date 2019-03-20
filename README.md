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

![CD4060 Pinout](https://github.com/jonathanrjpereira/CD4060-Timer/blob/master/img/pinout.png)
![CD4060 Pin Description](https://github.com/jonathanrjpereira/CD4060-Timer/blob/master/img/pindescription.png)

**Timing Cycle:**

![CD4060 RC Oscillator](https://github.com/jonathanrjpereira/CD4060-Timer/blob/master/img/ICBD.png)

R2 must satisfy the following equation: ![R2 R1](https://latex.codecogs.com/png.latex?2R_%7B1%7D%5Cleq%20R_%7B2%7D%20%5Cleq%2010R_%7B1%7D)

![time](https://latex.codecogs.com/png.latex?%5Clarge%20Time%20%3D%20t%20%3D%20%5Cfrac%7B2%5E%7Bn%7D%7D%7Bf_%7Bosc%7D%7D)

where n is the Output Number i.e. ![Qn](https://latex.codecogs.com/png.latex?%5Clarge%20Q_%7Bn%7D)

![Fosc](https://latex.codecogs.com/png.latex?f_%7Bosc%7D%20%3D%20%5Cfrac%7B1%7D%7B2.2%20%5Ctimes%20R_%7B1%7D%20%5Ctimes%20C_%7BX%7D%7D)

where 2.2 is the internal propagation delay.

## Circuit

![CD4060 Timer Block Diagram](https://github.com/jonathanrjpereira/CD4060-Timer/blob/master/img/BD.png)

The Timer IC requires the external RC network to be preconfigured in order to generate proper timing oscillations. External resets may be used to reset the timer. The time selector is configured to change the RC network value. The high power appliances are turned on when the relay is activated.

**Resistor Calculation:**

The table below shows the timing cycle of each output calculated by using the formulae given above.

![CD4060 Timer Resistor Calculation](https://github.com/jonathanrjpereira/CD4060-Timer/blob/master/img/time.png)

We can see that if we choose the value of R1 to be 1.9MΩ, we can obtain an output that varies from 14.79≈15sec to 4hr.

Similarly if we choose R1 to be 10.9MΩ, we obtain an output that varies from 1.4min to 24hr.

I wrote a small [Python script](https://github.com/jonathanrjpereira/CD4060-Timer/blob/master/time.py) to calculate the time delay for various resistance values including 1.9MΩ and 10MΩ.

![Schematic CD4060 Timer Circuit](https://github.com/jonathanrjpereira/CD4060-Timer/blob/master/img/sch.png)

As shown in the Resistor Calculation chart, we can get different time delays from the same output pins by simply changing the value of R. But we must also satisfy this equation ![R2 R1](https://latex.codecogs.com/png.latex?2R_%7B1%7D%5Cleq%20R_%7B2%7D%20%5Cleq%2010R_%7B1%7D) as explained earlier.

From this equation, we learn that if R = 1.9MΩ (1MΩ + 910KΩ), we must connect a suitable resistance of approximately 3.8MΩ-19MΩ to pin 11. Similarly if
R = 10.9MΩ (10MΩ + 910KΩ), we must connect a suitable resistance of approximately 21.8MΩ-109MΩ to pin 11. Hence we have chosen standard resistor values of 10MΩ and 22MΩ respectively.

We use a DPDT switch to toggle between these two resistor combinations. Note that the value of Cx i.e C5 is a constant 0.22uF and does not change by toggling the switch.

A 10-pin DIP switch is used to select a single output pin and connect it to the relay. Hence only when this pin goes HIGH, will the relay get activated.

C4 and R12 reset the timer when the circuit is turned ON through switch S4. The circuit can be reset (while being ON) by pressing the momentary switch S2.

The 7805 regulates the supply voltage from a 9V/12V source and LED11 indicates that the circuit is turned ON.

High power loads can be connected to the relays output terminals JP2. When the relay is not activated, the Common(COM) terminal is connected to Normally Closed(NC) terminal. But when the relay is activated, the Common(COM) terminal is connected to Normally Open(NO) terminal. LED12 is used to indicate whether the relay has been activated.

Transistor T1 acts as a switch an ensures sufficient drive current is provided to the relay. Diode D11 acts as a flyback diode which protects the transistor T1 from voltage spikes caused by the relay coil.

Capacitor's C1, C2 & C3 are used to filter noise in the supply line.

![Board](https://github.com/jonathanrjpereira/CD4060-Timer/blob/master/img/brd.png)

You can **Order the PCB:** []()

![Printable](https://github.com/jonathanrjpereira/CD4060-Timer/blob/master/img/print1.png)

Or you can printout the [PDF file](https://github.com/jonathanrjpereira/CD4060-Timer/blob/master/img/printable.pdf) and make your own PCB using the [Iron-on method]().

## Contributing🛠
Are you an engineer or hobbyist who has a great idea for a new feature in this project? Maybe you have a good idea for a bug fix? Feel free to grab our code & schematics from Github and tinker with it. Don't forget to smash ⭐️ & the Pull Request button.

[![alt text][1.1]][1] [![alt text][2.1]][2] [![alt text][3.1]][3]

[1.1]: https://github.com/jonathanrjpereira/Social-Media-README/blob/master/youtube.png (YouTube)
[2.1]: https://github.com/jonathanrjpereira/Social-Media-README/blob/master/instagram.png (Instagram)
[3.1]: https://github.com/jonathanrjpereira/Social-Media-README/blob/master/github.png (GitHub)

[1]: https://www.youtube.com/channel/UCRW-41O1vy98KKgJRQoYzdg
[2]: https://www.instagram.com/electroguruji/
[3]: https://github.com/jonathanrjpereira
