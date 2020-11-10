class channels:

    audio_file_struct = [[5, 5, 5, 5, 5, 5, 5, 5], [3, 0, 0, 0, 0, 0, 0, 0]]

    def __init__(self, tempo):
        self.tempo = tempo

    """this method will fill the sequence array depending on the
        which analog inputs yield values"""
    def scan_tracks(self):
        return
        
    def show_sequence(self):#does not work for some reason
        z = 0
        while z < 2: 
            print(self.audio_file_struct[z])
            z+=1

    def get_audio_num(self, x, y):
        return self.audio_file_struct[x][y]
            


