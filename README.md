
***
## <p align="center"> Hey we are team Astra we are 3, Rym, Adam, and Youssef, 15-year-old coders, and this is our repository. It comprises all the engineering materials for our autonomus vehicle model participating in the 2024 WRO Future Engineers competition. </p>

***

<div align=center>

![logo](./img/.png)

</div>

***
## The microcontroller:
<body>
  <div align=center>
    <h1>LEGO Mindstorms EV3 Brick</h1>
</div>
</body>

<table>
  <thead>
    <tr>
      <th>Feature</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Processor</td>
      <td>ARM9 processor running at 300 MHz</td>
    </tr>
    <tr>
      <td>Memory</td>
      <td>64 MB RAM, 16 MB flash storage</td>
    </tr>
    <tr>
      <td>Ports</td>
      <td>Four motor ports, four sensor ports</td>
    </tr>
    <tr>
      <td>Connectivity</td>
      <td>USB port, SD card slot, Bluetooth</td>
    </tr>
    <tr>
      <td>Display</td>
      <td>Monochrome LCD display</td>
    </tr>
    <tr>
      <td>Controls</td>
      <td>Buttons for navigation and control</td>
    </tr>
    <tr>
      <td>Software</td>
      <td>LEGO Mindstorms EV3 software, supports languages like Python and C++</td>
    </tr>
    <tr>
      <td>Use Cases</td>
      <td>Robotics education, hobbyist projects, competitions</td>
    </tr>
    <tr>
      <td>Community</td>
      <td>Large online community, resources, tutorials</td>
    </tr>
  </tbody>
</table>

***
<p align="center">
  <img width="320" height="300" src="https://m.media-amazon.com/images/I/31uzGocdrPL._AC_UF894,1000_QL80_.jpg">
</p>


  


***
## Our vehicle: 

We used the EV3 MINDSTORMS Educational kit. We chose to use a racing car shape so it could move fluidly and dodge the obstacles

A 3D model of the robot made in Studio 2.0 :

![finalfirstproduct](https://github.com/youssefelbaitar/WRO-Future-Engineers/assets/164657596/dbaef324-04d2-4831-9cfe-4c9155e96a13)


The final program/code for our autonomous vehicle can be found here: 


***
## Mobility Management

### Motor Selection and role
Choosing the motors is an important step to build the vehicle. We used only 1 big motor for the main movemement so the robot can be smaller and a mid motor for the steering mechanism so it allows the robot to turn easily while moving forward.

<body>
    <table>
        <tr>
            <th>Aspect</th>
            <th>EV3 Big Motor</th>
            <th>EV3 Mid Motor</th>
        </tr>
        <tr>
            <td>Size</td>
            <td>Large</td>
            <td>Medium</td>
        </tr>
        <tr>
            <td>Power</td>
            <td>High torque</td>
            <td>Medium torque</td>
        </tr>
        <tr>
            <td>Speed</td>
            <td>Lower</td>
            <td>Higher</td>
        </tr>
        <tr>
            <td>Applications</td>
            <td>Best suited for heavy-duty tasks like driving large wheels or lifting heavy objects.</td>
            <td>Well-suited for medium-duty tasks like controlling arms, gears, or small wheels.</td>
        </tr>
        <tr>
            <td>Weight</td>
            <td>Heavier</td>
            <td>Lighter</td>
        </tr>
    </table>

  
### Chassis 

We tried to copy f1 vehicles shape.The steering mechanism is located in the front, utilizes smaller wheels. Additionally, positioning the larger wheels as close to each other as possible, for more stability and agility.
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<body>
    <h3>Advantages of Different F1 Car Shapes</h3>
    <table>
        <tr>
            <th>Shape</th>
            <th>Advantages</th>
        </tr>
        <tr>
            <td>Aerodynamic</td>
            <td>
                <ul>
                    <li>Improved airflow over and around the car, reducing drag and increasing straight-line speed.</li>
                    <li>Enhanced downforce generated, improving grip and cornering stability.</li>
                    <li>Efficient cooling of engine and components due to optimized airflow.</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>Compact</td>
            <td>
                <ul>
                    <li>Reduced frontal area, minimizing air resistance and drag.</li>
                    <li>Improved agility and responsiveness in tight corners and chicanes.</li>
                    <li>Lower weight distribution, enhancing acceleration and braking performance.</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>Streamlined</td>
            <td>
                <ul>
                    <li>Smooth airflow around the car, reducing turbulence and drag.</li>
                    <li>Improved fuel efficiency and reduced fuel consumption.</li>
                    <li>Enhanced stability at high speeds, minimizing aerodynamic disturbances.</li>
                </ul>
            </td>
        </tr>
    </table>
</body>

<p align="center">

  
![robot hehe](https://github.com/youssefelbaitar/WRO-Future-Engineers/assets/164657596/08faa470-58ce-440f-a0d2-4ba979c20e14)


</p>

***
<h1> Sensors </h1>

Our vehicle is simple,with only two color sensor crucial for obstacle avoidance and turns.


  
### Vehicle Sensors Overview

<body>
    <table>
        <tr>
            <th>Sensor</th>
            <th>Purpose</th>
            <th>Functionality</th>
        </tr>
        <tr>
            <td>Color Sensor 1</td>
            <td>Turn Identification</td>
            <td>Reads colored lines (orange or blue) on the competition field to determine driving direction.</td>
        </tr>
        <tr>
            <td>Color Sensor 2</td>
            <td>Obstacle Detection</td>
            <td>Identifies obstacles by detecting red or green colors.</td>
        </tr>
    </table>
  </body>
<p align="center">
  
![1](https://github.com/youssefelbaitar/WRO-Future-Engineers/assets/164657596/a5cf38b7-1196-4f77-b6f1-67d52d299269)

</p>



