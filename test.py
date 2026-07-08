"""
DSA Prep Structure Generator
-----------------------------
Creates a folder-per-topic structure for DSA preparation.

Each folder gets:
  - 0_README.md with a checklist of topics
  - One Java placeholder file per topic
  - Files are numbered as:
        1_ArrayRotation.java
        2_KthLargestSmallest.java
        ...

Run:
    python setup_dsa_structure.py

Change ROOT_DIR below if you want the structure to be created somewhere else.
"""

import os

ROOT_DIR = "."  # Run this script inside your DSA_Prep folder

STRUCTURE = {
    "1_Arrays": [
        # "ArrayRotation", "KthLargestSmallest", "MajorityElement",
        # "FindDuplicates", "KadanesAlgorithm", "TwoSumProblem",
        # "MergeIntervals", "SubarraySumEqualsK", "TrappingRainWater",
        # "LongestConsecutiveSequence", "ProductOfArrayExceptSelf",
        # "SlidingWindowPattern"
    ],
    "2_Strings": [
        # "PalindromeCheck", "AnagramCheck", "StringReversal",
        # "LongestCommonSubstring", "LongestPalindromicSubstring",
        # "KMPAlgorithm", "RabinKarpAlgorithm", "GroupAnagrams",
        # "WordBreakProblem", "EditDistance", "MinimumWindowSubstring",
        # "LongestRepeatingSubsequence", "SlidingWindowOnStrings"
    ],
    "3_Recursion": [
        # "BasicsOfRecursion", "FactorialAndPower", "FibonacciRecursive",
        # "SumOfDigits", "ReverseStringRecursive", "ReverseLinkedListRecursive",
        # "TowerOfHanoi", "GenerateAllSubsequences",
        # "RecursionVsIteration", "TailRecursion"
    ],
    "4_LinkedLists": [
        # "SinglyLinkedList", "DoublyLinkedList", "CircularLinkedList",
        # "ReverseLinkedList", "DetectAndRemoveLoop", "MergeTwoSortedLists",
        # "IntersectionPoint", "RemoveNthNodeFromEnd", "PalindromeLinkedList",
        # "FlattenLinkedList"
    ],
    "5_StacksAndQueues": [
        # "StackImplementation", "QueueImplementation", "InfixToPostfix",
        # "BalancedParentheses", "NextGreaterElement",
        # "StackUsingQueues", "QueueUsingStacks", "LRUCache",
        # "CircularQueue", "SlidingWindowMaximum", "EvaluatePostfixExpression"
    ],
    "6_CollectionsFramework": [
        # "ArrayListVsLinkedList", "HashMapInternalWorking",
        # "HashSetVsTreeSetVsLinkedHashSet",
        # "HashMapVsTreeMapVsLinkedHashMap", "PriorityQueueUsage",
        # "ArrayDequeAsStackAndQueue", "StackVsArrayDeque",
        # "IteratorVsListIteratorVsForEach", "ComparableVsComparator",
        # "CollectionsUtilityMethods", "FailFastVsFailSafeIterators",
        # "ConcurrentCollectionsOverview"
    ],
    "7_Hashing": [
        # "HashMapImplementation", "CollisionResolutionTechniques",
        # "CountFrequencies", "TwoSumProblem", "SubarraySumEqualsK",
        # "GroupAnagrams", "FindDuplicateSubtrees", "FindItineraryFromTickets"
    ],
    "8_Trees": [
        # "BinaryTreeImplementation", "BSTImplementation",
        # "TreeTraversals", "LowestCommonAncestor", "DiameterOfBinaryTree",
        # "LevelOrderTraversal", "HeightOfBinaryTree", "InvertBinaryTree",
        # "TreeFromInorderPreorderPostorder", "CheckBalancedBinaryTree",
        # "SerializeDeserializeBinaryTree", "MaximumPathSum",
        # "KthSmallestElementInBST"
    ],
    "9_Graphs": [
        # "GraphRepresentation", "DFS", "BFS", "DijkstraAlgorithm",
        # "BellmanFordAlgorithm", "FloydWarshallAlgorithm",
        # "KruskalsMST", "PrimsMST", "TopologicalSorting",
        # "CycleDetection", "KosarajuSCC", "UnionFindAlgorithm",
        # "UnionFindApplications"
    ],
    "10_DynamicProgramming": [
        # "ZeroOneKnapsack", "LongestCommonSubsequence",
        # "LongestIncreasingSubsequence", "MatrixChainMultiplication",
        # "CoinChangeProblem", "RodCuttingProblem", "EditDistance",
        # "SubsetSumProblem", "PartitionEqualSubsetSum",
        # "WildcardMatching", "PalindromePartitioning"
    ],
    "11_Backtracking": [
        # "NQueensProblem", "RatInAMaze", "SudokuSolver", "WordSearch",
        # "GenerateAllPermutations", "CombinationSum",
        # "PartitionToKEqualSumSubsets", "HamiltonianCycle",
        # "SubsetsIIWithDuplicates", "PalindromePartitioning"
    ],
    "12_Greedy": [
        # "ActivitySelectionProblem", "HuffmanCoding", "JobSequencingProblem",
        # "FractionalKnapsackProblem", "MinimumNumberOfPlatforms",
        # "PrimsMST", "KruskalsMST", "DijkstraAlgorithm"
    ],
    "13_Searching": [
        # "LinearSearch", "BinarySearch", "TernarySearch",
        # "ExponentialSearch", "InterpolationSearch",
        # "BinarySearchOnAnswer", "DFS", "BFS"
    ],
    "14_Sorting": [
        # "BubbleSort", "SelectionSort", "InsertionSort",
        # "MergeSort", "QuickSort", "HeapSort", "RadixSort"
    ],
    "15_BitManipulation": [
        # "CountSetBits", "FindOnlyNonRepeatingElement",
        # "PowerOfTwoCheck", "FindTwoNonRepeatingElements",
        # "CountBitsToFlip", "DivideWithoutDivisionOperator",
        # "FindMissingNumber", "SwapWithoutTempVariable",
        # "PowerSetUsingBitwise", "ReverseBitsOfNumber"
    ],
    "16_MathematicalAlgorithms": [
        # "SieveOfEratosthenes", "EuclideanGCD", "LCMOfTwoNumbers",
        # "ModularExponentiation", "PrimeFactorization",
        # "FibonacciNumbers", "CatalanNumbers", "CheckIfPrime",
        # "CountDigitsInNumber", "PowerOfNumberUsingExponentiation"
    ],
    "17_Patterns": [
        # "PyramidPattern", "DiamondPattern", "PascalsTriangle",
        # "NumberPatterns", "AlphabetPatterns", "ZigzagPattern",
        # "ButterflyPattern"
    ],
    "18_Miscellaneous": [
        # "PigeonholePrinciple", "ReservoirSampling", "RandomizedQuickSort",
        # "FloydsCycleDetection", "ApproximateCounting",
        # "FindMissingNumber", "ShuffleAnArray", "TrieImplementation",
        # "MedianFromDataStream"
    ],
}

JAVA_TEMPLATE = """public class {class_name} {{

    // TODO: Implement {readable_name}

    public static void main(String[] args) {{

    }}
}}
"""


def to_readable(name):
    out = []
    for i, ch in enumerate(name):
        if ch.isupper() and i != 0:
            out.append(" ")
        out.append(ch)
    return "".join(out)


def create_structure(root_dir):
    os.makedirs(root_dir, exist_ok=True)

    top_readme = ["# DSA Preparation Tracker\n\n"]
    top_readme.append("## Topics\n\n")

    for folder, topics in STRUCTURE.items():
        folder_path = os.path.join(root_dir, folder)
        os.makedirs(folder_path, exist_ok=True)

        folder_name = folder.split("_", 1)[1]

        top_readme.append(f"- [{folder_name}](./{folder}) ({len(topics)} Topics)\n")

        # Folder README
        with open(os.path.join(folder_path, "0_README.md"), "w", encoding="utf-8") as f:
            f.write(f"# {folder_name}\n\n")
            f.write("## Checklist\n\n")
            for i, topic in enumerate(topics, start=1):
                f.write(f"- [ ] {i}. {to_readable(topic)}\n")

        # Java Files
        for i, topic in enumerate(topics, start=1):
            filename = f"{i}_{topic}.java"
            filepath = os.path.join(folder_path, filename)

            if not os.path.exists(filepath):
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(
                        JAVA_TEMPLATE.format(
                            class_name=topic,
                            readable_name=to_readable(topic),
                        )
                    )

    # Root README
    with open(os.path.join(root_dir, "0_README.md"), "w", encoding="utf-8") as f:
        f.writelines(top_readme)

    total_topics = sum(len(v) for v in STRUCTURE.values())

    print("=" * 50)
    print("DSA Structure Created Successfully!")
    print(f"Folders : {len(STRUCTURE)}")
    print(f"Java Files : {total_topics}")
    print("=" * 50)


if __name__ == "__main__":
    create_structure(ROOT_DIR)