Tutorial:
- https://www.youtube.com/watch?v=pHrwqLhAaMw
- https://github.com/glamp/ggplot-tutorial/

Docs/Examples:
- http://ggplot.yhathq.com/


##################### Needed to patch #######
## IMPORTANT ################################
# https://github.com/yhat/ggplot/issues/417 #
##############################################################################################
# got it working by changing "rows" to "index" in ggplot/stats/stat_bin.py, on line 126-127: #
# _wfreq_table = pd.pivot_table(_df, values='weights', rows=['assignments'], aggfunc=np.sum) #
##############################################################################################


OVERVIEW
- less popular than matplotlib
- The visual are nicer than matplotlib
- It uses "grammar of graphics"
- Works well with pandas
- Paramiters in the head adjuster per var but in the other layers they are hard coded

Grammar of Graphics
http://ggplot.yhathq.com/docs/index.html
- Geoms
- Stats
- Facets
- Scales
- Themes