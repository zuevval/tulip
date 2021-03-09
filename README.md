# Tulip
Pseudo-graphics for your `Contributions` graph

<img align="center" src="https://user-images.githubusercontent.com/23435506/110288426-09a00b80-7ff9-11eb-880f-f7bdae9c37d0.png" />

## Requirements

Python 3.6+

## Usage
Suppose there is an empty space on your `Cotributions` timeline:

![image](https://user-images.githubusercontent.com/23435506/110290185-86cc8000-7ffb-11eb-884b-aa2476bbd136.png)

You would like to add a funny picture like this:

![image](https://user-images.githubusercontent.com/23435506/110290597-00646e00-7ffc-11eb-8c26-ee267d0583a9.png)

To achieve this, follow the steps below.

1. Clone this repository locally: `git clone https://github.com/zuevval/tulip.git`
2. Create a new **empty** GitHub / GitLab repository, e. g. `github.com/your-name/tulip-impl`. You may make it private, but in this case, make sure that private contributions are set up to be displayed on your profile. Do not fork my repository because contributions to forks are not listed on the `Contributions` strip.
4. Modify `data.txt` so that it contains your image. The number corresponds to the color intensity. You may pick a template from the `examples` folder.
5. `python3 tulip.py --year [desired year]`, e. g. `python3 tulip.py --year 2016`
6. `git remote add impl [your-repository-url]`, e. g. `git remote add impl https://github.com/your-name/tulip-impl.git`
7. `git push --set-upstream impl main`

Now you should see the image on your profile!


## Removing the graphics

Simply delete the repository from your GitHub / GitLab profile.

## Troubleshooting
Should you have any questions or suggestions regarding Tulip, please [open an issue](https://github.com/zuevval/tulip/issues/new)

## Why "Tulip"?

This Python script has been written for the celebration of International Women Day 2021.
Tulip is one of the symbols of this day.
