{\rtf1\ansi\ansicpg1252\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 /*\
  Leaflet.AwesomeMarkers, a plugin that adds colorful iconic markers for Leaflet, based on the Font Awesome icons\
  (c) 2012-2013, Lennard Voogdt\
\
  http://leafletjs.com\
  https://github.com/lvoogdt\
*/\
\
/*global L*/\
\
(function (window, document, undefined) \{\
    "use strict";\
    /*\
     * Leaflet.AwesomeMarkers assumes that you have already included the Leaflet library.\
     */\
\
    L.AwesomeMarkers = \{\};\
\
    L.AwesomeMarkers.version = '2.0.1';\
\
    L.AwesomeMarkers.Icon = L.Icon.extend(\{\
        options: \{\
            iconSize: [35, 45],\
            iconAnchor:   [17, 42],\
            popupAnchor: [1, -32],\
            shadowAnchor: [10, 12],\
            shadowSize: [36, 16],\
            className: 'awesome-marker',\
            prefix: 'glyphicon',\
            spinClass: 'fa-spin',\
            extraClasses: '',\
            icon: 'home',\
            markerColor: 'blue',\
            iconColor: 'white'\
        \},\
\
        initialize: function (options) \{\
            options = L.Util.setOptions(this, options);\
        \},\
\
        createIcon: function () \{\
            var div = document.createElement('div'),\
                options = this.options;\
\
            if (options.icon) \{\
                div.innerHTML = this._createInner();\
            \}\
\
            if (options.bgPos) \{\
                div.style.backgroundPosition =\
                    (-options.bgPos.x) + 'px ' + (-options.bgPos.y) + 'px';\
            \}\
\
            this._setIconStyles(div, 'icon-' + options.markerColor);\
            return div;\
        \},\
\
        _createInner: function() \{\
            var iconClass, iconSpinClass = "", iconColorClass = "", iconColorStyle = "", options = this.options;\
\
            if(options.icon.slice(0,options.prefix.length+1) === options.prefix + "-") \{\
                iconClass = options.icon;\
            \} else \{\
                iconClass = options.prefix + "-" + options.icon;\
            \}\
\
            if(options.spin && typeof options.spinClass === "string") \{\
                iconSpinClass = options.spinClass;\
            \}\
\
            if(options.iconColor) \{\
                if(options.iconColor === 'white' || options.iconColor === 'black') \{\
                    iconColorClass = "icon-" + options.iconColor;\
                \} else \{\
                    iconColorStyle = "style='color: " + options.iconColor + "' ";\
                \}\
            \}\
\
            return "<i " + iconColorStyle + "class='" + options.extraClasses + " " + options.prefix + " " + iconClass + " " + iconSpinClass + " " + iconColorClass + "'></i>";\
        \},\
\
        _setIconStyles: function (img, name) \{\
            var options = this.options,\
                size = L.point(options[name === 'shadow' ? 'shadowSize' : 'iconSize']),\
                anchor;\
\
            if (name === 'shadow') \{\
                anchor = L.point(options.shadowAnchor || options.iconAnchor);\
            \} else \{\
                anchor = L.point(options.iconAnchor);\
            \}\
\
            if (!anchor && size) \{\
                anchor = size.divideBy(2, true);\
            \}\
\
            img.className = 'awesome-marker-' + name + ' ' + options.className;\
\
            if (anchor) \{\
                img.style.marginLeft = (-anchor.x) + 'px';\
                img.style.marginTop  = (-anchor.y) + 'px';\
            \}\
\
            if (size) \{\
                img.style.width  = size.x + 'px';\
                img.style.height = size.y + 'px';\
            \}\
        \},\
\
        createShadow: function () \{\
            var div = document.createElement('div');\
\
            this._setIconStyles(div, 'shadow');\
            return div;\
      \}\
    \});\
        \
    L.AwesomeMarkers.icon = function (options) \{\
        return new L.AwesomeMarkers.Icon(options);\
    \};\
\
\}(this, document));\
\
\
}