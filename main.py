import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from Constants import *

import colorama

pygame.init()

# -------------------------
# - Versions
ATLAS_MAJOR_VERSION: int = 1
ATLAS_MINOR_VERSION: int = 0
ATLAS_PATCH_VERSION: int = 0

print('PLBufferAtlas {}.{}.{}'.format(ATLAS_MAJOR_VERSION, ATLAS_MINOR_VERSION, ATLAS_PATCH_VERSION))

if 'pygame' not in dir():
   raise ImportError('PLBufferAtlas Required Pygame (2.0.0dev6 Recommended)')

class PLBufferAtlas:

   if 'colorama' in dir():
      OutputCode = {
            0: ('[Message]', )
      }

   # Not to be used during game play, only upon initialization

   """
   PLBufferAtlas is a Object that takes a list / dict of sprites
   Creates either both a new file, and surface or creates a surface with a preloaded file
   If you wish to be able to get specific images off the atlas, dict is recommended for string calls
   otherwise you are forced to use integer calls

   PLBufferGlue (PLBufferAtlas, PLBufferAtlas) returns <PLBufferAtlas(new)>
   the PLBufferAtlas contents are combined, PLBufferAtlas(2) left anchors to the ending surf width of PLBufferAtlas(1)
   New PLBufferAtlas Created
   * EnforceMemoryAllocations are added

   Memory Management

   EnforceMemoryAllocation(int)
      - PLBufferAtlas behavior slightly changes, functions like above however if the number of bytes allocated exceeds integer <bytes>
         it will drop the rest of the information
         * if an image is dropped during processing, it will be completely removed from the surface
   """

   def __init__(self, File : str, Sprites : list or dict):

      self.File = File
      self.Sprites = Sprites
      self.Bytes = 0

      print('PLBufferAtlas Packing ' , Sprites)



PLBufferAtlas('Assets.png', ({
      'Grass': 'Grass.png',
      'Dirt': 'Dirt.png'
}))