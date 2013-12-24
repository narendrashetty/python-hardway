class Song(object):

	def __init__ (self, lyrics):
		self.lyrics = lyrics
		
	def print_song(self):
		for ln in self.lyrics:
			print ln
		
a = Song(["Line1",
				"Line2",
				"Line3"])
				
b = Song(["New_Line1",
				"New_Line2",
				"New_Line3"])
				
a.print_song()

b.print_song()