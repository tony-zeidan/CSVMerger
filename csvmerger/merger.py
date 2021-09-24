from typing import List, Union
from pandas import read_csv, concat, DataFrame
import argparse
import os


def csvs_from_directory(directory: str) -> List[DataFrame]:
    """Reads all the csv files in a directory and returns them as a list of DataFrame objects.

    :param directory: The directory containing csv files
    :type directory: str
    :return: The list of read csv files
    :rtype: List[DataFrame]
    """
    return [read_csv(f) for f in [os.path.join(directory, ff) for ff in os.listdir(directory)] if f.endswith(".csv")]


def merge_dfs(dfs: List[DataFrame], axis: int = 0) -> DataFrame:
    """Merges a directory of csv files together.

    :param dfs: The list of DataFrame objects to merge
    :type dfs: List[DataFrame]
    :param axis: The axis to concatenate on (0 = vertical, 1 = horizontal)
    :type axis: int
    :return: The merged DataFrame object
    :rtype: DataFrame
    """
    masterdf = concat(dfs, ignore_index=True, axis=axis)
    masterdf.drop_duplicates(inplace=True, ignore_index=True)
    return masterdf


def df_to_csv(df: DataFrame, output_path: str, include_index: bool = False):
    """Outputs a DataFrame to a filepath (wrapper).

    :param df: The dataframe to output
    :type df: DataFrame
    :param output_path: The path to output the csv at
    :type output_path: str
    :param include_index: Whether to include the index in the output or not
    :type include_index: bool
    """
    df.to_csv(output_path, index=include_index, index_label="ind")


def merge_csvs_from_directory(directory: str, output_path: str = None,
                              axis: int = 0, include_index: bool = False) -> Union[None, DataFrame]:
    """Reads csv files from a directory, merges them, and outputs the result.

    :param directory: The directory containing the csv files
    :type directory: str
    :param output_path: The output path for the merged csv (None->return object)
    :type output_path: str
    :param axis: The axis to concatenate on (0 = vertical, 1 = horizontal)
    :type axis: int
    :param include_index: Whether to include the index in the output or not
    :type include_index: bool
    :return: The merged csv as a DataFrame object (output_path=None)
    :rtype: Union[None, DataFrame]
    """
    dfs = csvs_from_directory(directory)
    masterdf = merge_dfs(dfs, axis=axis)
    if output_path:
        df_to_csv(masterdf, output_path, include_index=include_index)
    else:
        return masterdf


def main():
    parser = argparse.ArgumentParser(prog='csv-merger', usage='%(prog)s [options]',
                                     description="Input a directory of csv files to merge them.")
    parser.add_argument('dir', type=str, metavar="directory", help='path to directory containing csv files')
    parser.add_argument('out', type=str, metavar="output", help='path to output merged csv file')
    parser.add_argument('-a', '--axis', metavar='axis', type=int, nargs=1, default=0,
                        help='the axis to concatenate on (0 = vertical, 1 = horizontal)')
    parser.add_argument('-i', '--index', dest='index', action='store_const',
                        const=True, default=False, help='whether to include the index in the output or not')
    args = parser.parse_args()

    merge_csvs_from_directory(args.dir, args.out, axis=args.axis, include_index=args.index)
    print("Run finished.")


if __name__ == '__main__':
    main()
