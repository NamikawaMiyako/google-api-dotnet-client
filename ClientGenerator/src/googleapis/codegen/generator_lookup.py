#!/usr/bin/python2.7
# Copyright 2012 Google Inc. All Rights Reserved.
#

"""Common generator index utilities."""

__author__ = 'akesling@google.com (Alex Kesling)'


from googleapis.codegen import csharp_generator


# Multiple generators per language are possible, as is the case with
# Java below. Template trees can specify a specific generator in their
# features.json file (with the "generator" attribute); this will refer
# to a key in these dictionaries.  If a template tree does not
# include this specification, the language name is used as a key.
_GENERATORS_BY_LANGUAGE = {
    'csharp': csharp_generator.CSharpGenerator,
    }


_ALL_GENERATORS = {
}


_ALL_GENERATORS.update(_GENERATORS_BY_LANGUAGE)


def GetGeneratorByLanguage(language_or_generator):
  """Return the appropriate generator for this language.

  Args:
    language_or_generator: (str) the language for which to return a generator,
        or the name of a specific generator.

  Raises:
    ValueError: If provided language isn't supported.

  Returns:
    The appropriate code generator object (which may be None).
  """

  try:
    return _ALL_GENERATORS[language_or_generator]
  except KeyError:
    raise ValueError('Unsupported language: %s' % language_or_generator)


def SupportedLanguages():
  """Return the list of languages we support.

  Returns:
    list(str)
  """
  return sorted(_GENERATORS_BY_LANGUAGE)
