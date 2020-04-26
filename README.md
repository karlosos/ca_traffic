# Cellular Automata Traffic Simulation

Simulating traffic with cellular automata. Creating roads systems and 

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


#### Simulation tweaking

Edit `simulation.py`. Create roads, generators and terminators.
Terminator is used as a black hole (road where cells disappear). 
Connect objects (such as lanes, generators and terminators) with `Lane.link(lane1, lane2)`.

Run with `python simulation.py`.


## Contruburing 

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
