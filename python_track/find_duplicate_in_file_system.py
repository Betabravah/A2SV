class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        _dict = defaultdict(lambda: [])
        for path in paths:
            temp = path.split(' ')
            root, files = temp[0], temp[1:]
            
            for file in files:
                content = []
                new_file = []
                index = 0
                while index < len(file)-1:
                    if file[index] == '(':
                        index += 1
                        while index < len(file)-1:
                            content.append(file[index])
                            index += 1
                    else:
                        new_file.append(file[index])
                    index += 1
                    
                content = ''.join(content)
                new_file = ''.join(new_file)
                new_file = root + '/' + new_file

                
                _dict[content].append(new_file)
        
        duplicates = []
        for content in _dict:
            file_paths = _dict[content]
            if len(file_paths) > 1:
                duplicates.append(file_paths)

        return duplicates
