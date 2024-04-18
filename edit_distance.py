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
        print(f"Test {iteration}: correct")
    else:
        print(f"Test {iteration}: incorrect")

def main() -> None:
    a = edit_distance("aa", "bb")
    print(a)
    
if __name__ == '__main__':
    main()