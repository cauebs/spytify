# If no scope is specified, access is permitted only to publicly available
# information: that is, only information normally visible to normal logged-in
# users of the Spotify desktop, web, and mobile clients
# (e.g. public playlists).

# Read access to user's private playlists.
PLAYLIST_READ_PRIVATE = 'playlist-read-private'

# Include collaborative playlists when requesting a user's playlists.
PLAYLIST_READ_COLLABORATIVE = 'playlist-read-collaborative'

# Write access to a user's public playlists.
PLAYLIST_MODIFY_PUBLIC = 'playlist-modify-public'

# Write access to a user's private playlists.
PLAYLIST_MODIFY_PRIVATE = 'playlist-modify-private'

# Control playback of a Spotify track. This scope is currently only available
# to Spotify native SDKs (for example, the iOS SDK and the Android SDK).
# The user must have a Spotify Premium account.
STREAMING = 'streaming'

# Write/delete access to the list of artists and other users
# that the user follows.
USER_FOLLOW_MODIFY = 'user-follow-modify'

# Read access to the list of artists and other users that the user follows.
USER_FOLLOW_READ = 'user-follow-read'

# Read access to a user's "Your Music" library.
USER_LIBRARY_READ = 'user-library-read'

# Write/delete access to a user's "Your Music" library.
USER_LIBRARY_MODIFY = 'user-library-modify'

# Read access to user’s subscription details (type of user account).
USER_READ_PRIVATE = 'user-read-private'

# Read access to the user's birthdate.
USER_READ_BIRTHDATE = 'user-read-birthdate'

# Read access to user’s email address.
USER_READ_EMAIL = 'user-read-email'

# Read access to a user's top artists and tracks
USER_TOP_READ = 'user-top-read'
