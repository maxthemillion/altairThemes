def standardTheme():
    # Typography
    font = "Arial"
    labelFont = "Arial" 
    sourceFont = "Arial"
    fontColor = '#4d4d4d'
    # Axes
    axisColor = "#DEDDDD"
    gridColor = "#DEDDDD"
    markColor = "#1696d2"
    background = 'white'

    titleFontSize = 20
    titleFontWeight=300
    subTitleFontSize = 15
    axisTitleFontSize = 12
    axisTitleFontWeight=400
    textFontSize = 12
    labelFontSize = 10

    # Colors
    main_palette = ["#a6cee3", 
                    "#1f78b4",
                    "#b2df8a", 
                    "#33a02c", 
                    "#fb9a99", 
                    "#e31a1c", 
                    "#fdbf6f", 
                    "#ff7f00", 
                   ]
    sequential_palette = ["#cfe8f3", 
                          "#a2d4ec", 
                          "#73bfe2", 
                          "#46abdb", 
                          "#1696d2", 
                          "#12719e", 
                         ]
    return {
        "padding": {"left": 5, "top": 50, "right": 5, "bottom": 5},
        "width":500,
        "height":500,
        "config": {
            "title": {
                "fontSize": titleFontSize,
                "lineHeight": 100,
                "fontWeight": titleFontWeight,
                "font": font,
                "anchor": "start", # equivalent of left-aligned.
                "color": fontColor,
                "offset": 30,
            },
            "guide-title":{
              "color": "Monospace",
              "fontSize": subTitleFontSize,
              "font": labelFont
            },
            "axisX": {
                "domain": True,
                "domainColor": axisColor,
                "domainWidth": 1,
                "grid": False,
                "domainDashOffset": 10,
                "labelFont": labelFont,
                "labelFontSize": labelFontSize,
                "labelAngle": 0, 
                "tickColor": axisColor,
                "titleFont": font,
                "titleFontSize": axisTitleFontSize,
                "titleFontWeight": axisTitleFontWeight,
                "titlePadding": 10, 
            },
            "axisY": {
                "domain": False,
                "grid": True,
                "gridColor": gridColor,
                "gridWidth": 1,
                "gridDash":[5,2],
                "domainDashOffset": 10,
                "labelFont": labelFont,
                "labelFontSize": labelFontSize,
                "labelAngle": 0, 
                "titleFont": font,
                "titleFontSize": axisTitleFontSize,
                "titleFontWeight": axisTitleFontWeight,
                "titlePadding": 10, 
            },
            "range": {
                "category": main_palette,
                "diverging": sequential_palette,
            },
            "legend": {
                "labelFont": labelFont,
                "labelFontSize": textFontSize,
                "symbolType": "circle",
                "symbolSize": 50,
                "titleFont": font,
                "titleFontSize": axisTitleFontSize,
                "title": "", # set it to no-title by default
                # "orient": "top-left", # so it's right next to the y-axis
                # "offset": 0, # literally right next to the y-axis.
            },
            "view": {
                'strokeWidth':0, #border around charts. to show, set the border to >0
            },

            ### MARKS CONFIGURATIONS ###
            "area": {
               "fill": markColor,
           },
           "line": {
               "color": markColor,
               "stroke": markColor,
               "strokeWidth": 1,
           },
           "trail": {
               "color": markColor,
               "stroke": markColor
           },
           "path": {
               "stroke": markColor,
           },
           "point": {
               "filled": True,
           },
           "text": {
               "font": sourceFont,
               "color": markColor,
               "fontSize": textFontSize,
               "align": "right",
               "fontWeight": 400,
               "size": 11,
           }, 
           "bar": {
                "fill": markColor,
                "strokeWidth": 0,
            },
            "header":{
                "titleFontSize": axisTitleFontSize,
                "titleFontWeight": axisTitleFontWeight
            }
        }
    }