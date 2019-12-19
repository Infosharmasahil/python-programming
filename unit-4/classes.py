import json

#create a class
class Person:
    #every class must have an init method
    def __init__(self, name, age):
        #print('person object initialized')
        self.name = name
        self.age = age

    def say_hello(self):
        print('Hello my name is {} and I am {} years old'.format(self.name, self.age))



#how to instantiate a class (create an object)
p = Person('John', 35)
q = Person('Jane', 28)
print(p.name)
print(p.age)

print(q.name)

#use a class method
p.say_hello()
q.say_hello()

#print(type(p))

#creat a rectangle class
#it shouldhave a length and a width
#it should have tow methods, perimeter and area

class rectangle:
    def __init__(self, length, width):

        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

r = rectangle(10, 20)
print(r.area())

print(r.perimeter())

print('Area is {}, perimeter is {}'.format(r.area(), r.perimeter()))



#create a playlist class
#the playlist has a name and a list of tracks
#each track is a dictionary, with title, artiste,length of track

#write methods to add a track, to remove a track, to shuffle the playlist

track_file_name = 'tracks.json'
class playlist:
    def __init__(self, name):
        self.name = name
        self.tracks = []

    def add_track(self, title, artist, length):
        track = {}
        track['title'] = title
        track['artist'] = artist
        track['length'] = length
        self.tracks.append(track)

  #  def remove_track(self, name):
   #     pass

    def remove_track(self, title):
        for idx in range(len(self.tracks)):
            if title == self.tracks[idx]['title']:

                break
        self.tracks.pop(idx)


    def save_tracks(self):

        #open file for writing
        with open(track_file_name, 'w') as track_file:
                track_file.write(json.dumps(self.tracks))

    def load_tracks(self):
        #load the data from the tracks.txt file
        with open('tracks.json', 'r') as track_file:
            data = json.load(track_file)
        #set the class tracks variable to the data loaded in 
        self.tracks = data

        pass





new_playlist = playlist('new music')

new_playlist.load_tracks()

print(new_playlist.tracks)


'''
p1 = playlist('tunes')
    
p1.add_track('shape of you', 'Ed Sheeren', 3.45)
p1.add_track('mamacita', 'Tyga, Santanta, YG', 4.15)

p1.save_tracks()

print(p1.tracks)



#pl.remove_track('Shape of You')

#print(pl.tracks)
'''