#!/usr/bin/env python

from os import path
from PIL import Image
import numpy as np
import os
from wordcloud import WordCloud

def main():
  module = AnsibleModule(
    argument_spec=dict(
      image_file = dict(required=True),
      mask_file = dict(required=False),
      background_color = dict(required=False, default='black'),
      contour_color = dict(required=False, default='white'),
      word_file = dict(required=True),
      ),
      supports_check_mode=False
  )
  try:
    image_file = module.params['image_file']
    mask_file = module.params['mask_file']
    background_color = module.params['background_color']
    contour_color = module.params['contour_color']
    word_file = module.params['word_file']

    # get data directory (using getcwd() is needed to support running example in generated IPython notebook)
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    # Read the whole text.
    text = open(path.join(d, word_file)).read()    
    
    ansible_mask = np.array(Image.open(path.join(d, mask_file)))
    wc = WordCloud(background_color=background_color, max_words=2000, mask=ansible_mask, contour_color=contour_color)
    wc.generate(text)
    
    wc.to_file(path.join(d, image_file))
    module.exit_json(changed=True)
  except:
    module.fail_json(msg=sys.exc_info()[0])
    

from ansible.module_utils.basic import *
main()



