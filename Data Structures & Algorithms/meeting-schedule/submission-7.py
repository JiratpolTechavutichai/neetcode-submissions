class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        # Sort the intervals explicitly by their start times
        intervals.sort(key=lambda x: x.start)
        
        # Check every interval starting from the second one
        for i in range(1, len(intervals)):
            # If current meeting starts before the previous one finishes
            if intervals[i].start < intervals[i - 1].end:
                return False
                
        return True