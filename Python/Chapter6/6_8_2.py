import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--edge',default = 10, type = int, help='边长')
args = parser.parse_args()
area = args.edge **2
print("面积 = ", area)
