import random
import time
import matplotlib.pyplot as plt
import string

def edit_distance(source: str, target: str) -> int:
    source_index: int = len(source)
    target_index: int = len(target) 

    
    if source_index == 0 or target_index == 0: 
        return source_index + target_index
    
    if  source[source_index - 1] == target[target_index - 1]:
        return edit_distance(source[:source_index - 1], target[:target_index - 1])
    
    else:
   
        return  1 + min(edit_distance(source[:source_index - 1], target), 
                    edit_distance(source, target[:target_index - 1]),
                    edit_distance(source[:source_index - 1], target[:target_index - 1]))

def compare(iteration: int, test_value: int, result: int) -> None:
    if test_value == result:
        print(f"Test {iteration}: correct, espected {test_value} - get {result}")
    else:
        print(f"Test {iteration}: incorrect, espected {test_value} - get {result}")

def test() -> None:
    with open("input.txt", "r") as input, open("output.txt", "r") as output:
        line = input.readline()
        
        it: int = 0
        while line:
            it += 1

            source, target = line.strip().split("-")
            result = int(output.readline())

            test_value = edit_distance(source, target)
            compare(it, test_value, result)

            line = input.readline()
        
def get_random_string(length: int) -> str:
    return ''.join(random.choices(string.ascii_lowercase, k = length))

def main() -> None:
    plt.style.use("_mpl-gallery")    
    fig, ax = plt.subplots()
    
    ax.set_title("Edit Distance")
    ax.set_xlabel("String Length")
    ax.set_ylabel("Time (ms)")
    
    max_length: int = int(input("Enter the maximum length of the string: "))
    max_repeat: int = int(input("Enter the maximum number of repeats: "))
    
    averages_results: list = []
    lengths: list = []
    for i in range(max_length + 1):
        results: list = []
        for j in range(max_repeat):
            source: str = get_random_string(i)
            target: str = get_random_string(i)
            
            start = time.time()
            edit_distance(source, target)
            end = time.time()          
            delta_time = (end - start)*1000
            
            print(f"Length: {i}, Repeat: {j}, Time: {delta_time} ms")                                      
            results.append(delta_time)

        averages_results.append(sum(results) / len(results))
        lengths.append(i)

        
        
    for i in range(max_length):
        print(f"Length: {lengths[i]}, Average Time: {averages_results[i]} ms")
    ax.plot(lengths, averages_results, label = "Edit Distance")
    
    plt.show()


if __name__ == '__main__':
    #test()
    main()
    