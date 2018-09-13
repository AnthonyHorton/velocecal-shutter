# velocecal-shutter
Python script for control of the VeloceCal shutter via the temporary Raspberry Pi set up.

## Installing

### With git

```
git clone https://github.com/AnthonyHorton/velocecal-shutter.git
cd velocecal-shutter
pip install -r requirements.txt
```

If not using a conda/pyvenv/virtualenv environment then add the `--user` option to the `pip install`
step.

### Without git

```
wget https://github.com/AnthonyHorton/velocecal-shutter/archive/master.zip
unzip velocecal-shutter-master.zip
cd velocecal-shutter
pip install -r requirements.txt
```

Then link to `shutter-run.py` from somewhere in your path, e.g. `sudo ln -s shutter-run.py /usr/local/bin/`.


## Running

Default operation is to start immediately, and open the shutter twice, once at the start and once at the end of the sequence. To do this just specify the total shutter open time and total elapsed time,
both in seconds.

```
shutter-run.py <total shutter open time> <total elapsed time>
```

There are options to delay the start of the sequence, change the number of times the shutter opens,
and change the hostname/IP of the Raspberry Pi.  For a fill list of arguments/options
```
shutter-run.py --help
```


## Updating

### With git

```
cd velocecal-shutter
git pull
```


### Without git

Reinstall as above.
