// url = 'ignoreURLParametersMatching'
function get_authkey(url){
    const precachedURL = getCacheKeyForURL(url, {
      cleanURLs,
      directoryIndex,
      ignoreURLParametersMatching,
      null,
    }
};