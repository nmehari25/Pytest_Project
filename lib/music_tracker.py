class MusicTracker:

    def __init__(self):
        self._tracks = []
        #   name: string
        # Side effects:
        #   Sets the name property of the self object

    def add(self, track):
        # Parameters:
        #   track: string representing a single track
        # empty list
        if track == "" or None:
            raise Exception ("No track entered.")
        # wrong type of input
        if not isinstance(track, str):
            raise Exception("Track is not in string format.")
        # remove empty, None, or non-string types from list
        elif track is Exception in self._tracks:
            return self._tracks.remove(track)
        # append additional tracks to list
        else: 
            self._tracks.append(track)
        # print("line 23 output of code with Exception")
        # print(self._tracks)

    def list(self):
        return self._tracks


