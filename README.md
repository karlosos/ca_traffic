# Cellular Automata Traffic Simulation

Simulating traffic with cellular automata. Creating roads systems and measure traffic.

Main window with editor:

![https://i.imgur.com/8GCigcr.png](https://i.imgur.com/8GCigcr.png)

Simulation window:

![https://i.imgur.com/2FbZJqf.png](https://i.imgur.com/2FbZJqf.png)

## Usage

Create virtual environment with `virtualenv`:

```
virtualenv .venv
```

Activate virtual environemnt:

```
source .venv/bin/activate
```

Or on windows:

```
.venv\Scripts\activate.bat
```

Then install packages with:

```
pip install -r requirements.txt
```

Now you have successfully configured your environment.

## Running the application

Run `main.py` with:

```
python main.py
```

## Using the application
![https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/f1013e1a-1f14-4736-9f97-d84c2e3b7355/ded8n9t-ec71cadb-8f60-44a9-b2e9-9097f7757461.png/v1/fill/w_1247,h_641,q_70,strp/interface_instr_by_autor52_ded8n9t-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3siaGVpZ2h0IjoiPD02NTgiLCJwYXRoIjoiXC9mXC9mMTAxM2UxYS0xZjE0LTQ3MzYtOWY5Ny1kODRjMmUzYjczNTVcL2RlZDhuOXQtZWM3MWNhZGItOGY2MC00NGE5LWIyZTktOTA5N2Y3NzU3NDYxLnBuZyIsIndpZHRoIjoiPD0xMjgwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.16nL50rD70rYiBRaBM3uLLD-kIDywmJCEgXyOVx9bpc](https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/f1013e1a-1f14-4736-9f97-d84c2e3b7355/ded8n9t-ec71cadb-8f60-44a9-b2e9-9097f7757461.png/v1/fill/w_1247,h_641,q_70,strp/interface_instr_by_autor52_ded8n9t-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3siaGVpZ2h0IjoiPD02NTgiLCJwYXRoIjoiXC9mXC9mMTAxM2UxYS0xZjE0LTQ3MzYtOWY5Ny1kODRjMmUzYjczNTVcL2RlZDhuOXQtZWM3MWNhZGItOGY2MC00NGE5LWIyZTktOTA5N2Y3NzU3NDYxLnBuZyIsIndpZHRoIjoiPD0xMjgwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.16nL50rD70rYiBRaBM3uLLD-kIDywmJCEgXyOVx9bpc)

The interface has 12 elements with following functions:
1. File - allows user to save the model currently on canvas or load an existing one from the hard drive
2. Preview of part - previews the currently loaded block (blocks are like brushes in painting apps, but this time, they're predefined road mini models)
3. Load model - button that readies the currently selected mini model for use on the canvas
4. Block selection - this is where user selects the block they want to use for modelling (the blocks will be described in the next section)
5. Max steps - defines the length of the simulation (in iterations)
6. Cars - defines how many car models should spawn in the simulation
7. Start simulation - button that runs the simulation using chosen parameters and current model on canvas
8. Resize map x y - fields used for input of the desired simulation map size (in pixels/cells)
9. Resize map - button 
10. Turn probability editing on/off - A button used for editing the probability on road cells with more than 1 direction (first click enables edit mode, the next disables it)
11. Turn probability - field used to input the chance (in %) with which the car should choose the default option (first direction) on the intersection, the default option is defined by the oldest road block placed on the given cell.
12. The canvas - allows the user to "paint" the desired traffic model using blocks 

After the "Start simulation" button is pressed, the user will be shown real-time visualization of of the traffic movement on the model. The simulation may be canceled at any time by pressing the "Esc" key. Every iteration, the app collects data on the status of every car in the simulation, as well as global statistics. After the simulation is over, the app saves all the results to the "Results" folder and shows the user the visualization of the final state of the simulation, as well as heat maps of traffic flow and traffic jams.

### Blocks
As of the moment of writing this section, the app supports a choice of 20 pre-defined blocks:
1. Generate straight-road - a flexible block that generates a straight road using given parameters (the road can be up to 3 pixels wide, meaning 3 cars can move through it in parallel and an indefinite length).
2. cross-section - A basic cross section of 2 one-way roads.
3. cross-section-X - A cross section of 2 bidirectional roads.
4. traffic-circle - A basic roundabout with a width of 1 pixel
5. cross-section T-up - cross section T model facing north
6. cross-section T-down - cross section T model facing south
7. cross-section T-left - cross section T model facing west
8. cross-section T-right - cross section T model facing east
9. eraser - a blank block with flexible size, can be used to erase part of the model
10. Measuring flag - a block used to set up a flag of flexible size that measures traffic jams in an area
11. Cross-section-X-lights - cross section X model with traffic lights
12. cross-section-T-up-lights - cross section T model facing north with traffic lights
13. cross-section-T-down-lights - cross section T model facing south with traffic lights
14. cross-section-T-left-lights - cross section T model facing west with traffic lights
15. cross-section-T-right-lights - cross section T model facing east with traffic lights
16. traffic-light - a block used to set up a traffic light at selected position in the model
17. priority - a block used to add or remove priority on the selected road cell
18. starting_point - a block used to define the spawning point of car models, including the chance at which they'll use it instead of the other ones
19. Part flow measurement - a block used to place a flag with flexible size that collects data on traffic flow in the selected area
20. Double roundabout - A basic roundabout with a width of 2 pixels, also has smaller size compared to the other one

### Workflow
To start modelling all a user has to  do is to select a block and load it. Some blocks are flexible, meaning their parameters can be adjusted. It is then possible to place as many copies of this block as necessary. When two blocks intersect on a cell, their directions are summed (for example, if 2 straight roads intersect, they form an intersection). The default action (direction) is then defined by the oldest road on a given cell, while the other direction is treated as an alternative. Each cell can have up to 2 directions to choose from. 
The model size can be adjusted on the go, however it's worth noting that if there are any road cells beyond the new model size(when reducing the size), they will be deleted.
It is recommended to place the measuring flags after the model is finished (and optionally saved) as they cannot be deleted.
Every model requires a placement of at least 1 starting point. The starting points can be added and removed using the same tool. Each of those points requires specifying an intensity, so it is recommended to either carefully plan their placement or experiment with a previously saved copy of the model.
Once the model is finished, the user can specify the parameters of the simulation (maximum steps and car number). Once those are satisfactory, the simulation can be started by pressing the appropriate button.
The user can either wait for the simulation to end or cancel it early in case of collecting a satisfactory amount of data. The results are then saved to a subfolder with name based on the starting time of the simulation, under the "Results" folder.

## Contributing 

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
