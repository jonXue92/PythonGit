# -*- coding: utf-8 -*-

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
class Insert:
    def insert(self, intervals, newInterval):
        answer = []
        
        index = 0
        while index < len(intervals) and intervals[index].start < newInterval.start:
            index += 1
            intervals.insert(index, newInterval)
            
        last = None
        for item in intervals:
            if last == None or last.end < item.start:
                answer.append(item)
                last = item
            else:
                last.end = max(last.end, item.end)
                
        return answer