import math
import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("flange_diameter",
                        help="flange diameter in mm", type=float)
    parser.add_argument("center_flange_distance",
                        help="distance from flange to hub centerline in mm", type=float)
    parser.add_argument("effective_rim_diameter",
                        help="diameter of spoke bed in rim, in mm", type=float)
    parser.add_argument("--spokes", help="number of spokes",
                        type=int, default=32)
    parser.add_argument(
        "--cross", help="lacing pattern, omit for radial lacing", type=int, default=0)
    args = parser.parse_args()
    print(calc_spoke_length(args.flange_diameter, args.center_flange_distance,
          args.effective_rim_diameter, args.spokes, args.cross))


def main_interactive():
    flange_diameter = float(input("Enter flange diameter: "))
    center_flange_distance = float(input("Enter center-flange distance: "))
    effective_rim_diameter = float(input("Enter ERD: "))
    spoke_count = float(input("Enter number of spokes: "))
    cross = int(
        input("Enter lacing pattern, between 1 and 4. Enter 0 for radial lacing: "))
    spoke_length = calc_spoke_length(
        flange_diameter, center_flange_distance, effective_rim_diameter, spoke_count, cross)
    print("Spoke length is {:.1f}".format(spoke_length))


def calc_spoke_length(fd, cfd, erd, spokes, cross):
    if fd <= 0 or cfd < 0 or erd <= 0 or spokes <= 0 or cross < 0:
        raise ValueError("Invalid input!")
    elif spokes % 4 != 0:
        raise ValueError("Spoke count must be a multiple of 4!")
    elif cross > 0 and spokes/cross < 10:
        raise ValueError("Too much spoke head overlap due to lacing pattern!")
    elif erd <= fd:
        raise ValueError("Flange diameter must be less than ERD!")
    if cross == 0:
        return math.sqrt(math.pow((erd - fd)/2.0, 2) + math.pow(cfd, 2))
    else:
        angle = 720.0/spokes * cross
        return math.sqrt(math.pow(erd/2.0, 2) + math.pow(fd/2.0, 2) - ((erd * fd)/2.0) * math.cos(angle * math.pi/180) + math.pow(cfd, 2))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main()
    else:
        try:
            main_interactive()
        except KeyboardInterrupt:
            print("User cancelled!")
        except ValueError as err:
            print(err)
