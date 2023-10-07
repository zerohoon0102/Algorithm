class Cell:
    def __init__(self, key:int, value: int):
        self.key = key
        self.value = value
        self.leftCell = None
        self.rightCell = None

    def updateValue(self, value: int):
        self.value = value

    def getValue(self):
        return self.value
    
    def getKey(self):
        return self.key
    
    def getRightCell(self):
        return self.rightCell

    def setRightCell(self, cell):
        self.rightCell = cell
    
    def getLeftCell(self):
        return self.leftCell

    def setLeftCell(self, cell):
        self.leftCell = cell
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cacheCell = {}
        self.leastUsedCell = None
        self.recentUsedCell = None

    def renew(self, key: int) -> int:
        cell = self.cacheCell[key]
        if cell != self.recentUsedCell:
            # pop cell
            leftCell = cell.getLeftCell()
            rightCell = cell.getRightCell()
            if leftCell:
                leftCell.setRightCell(rightCell)
            if rightCell:
                rightCell.setLeftCell(leftCell)
                if cell == self.leastUsedCell:
                    self.leastUsedCell = rightCell
            
            # put cell
            self.recentUsedCell.setRightCell(cell)
            cell.setLeftCell(self.recentUsedCell)
            self.recentUsedCell = cell
    
    def get(self, key: int) -> int:
        if key in self.cacheCell:
            self.renew(key)

            return self.cacheCell[key].getValue()
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cacheCell:
            cell = Cell(key, value)

            if not self.leastUsedCell:
                self.leastUsedCell = cell
            else:
                self.recentUsedCell.setRightCell(cell)
                cell.setLeftCell(self.recentUsedCell)
            
            self.recentUsedCell = cell
            self.cacheCell[key] = cell

            if len(self.cacheCell) > self.capacity:
                nxtLeastCell = self.leastUsedCell.getRightCell()
                del self.cacheCell[self.leastUsedCell.getKey()]
                self.leastUsedCell = nxtLeastCell
        else:
            cell = self.cacheCell[key]
            cell.updateValue(value)
            self.renew(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
