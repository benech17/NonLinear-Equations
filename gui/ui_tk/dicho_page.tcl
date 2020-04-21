#############################################################################
# Generated by PAGE version 5.1
#  in conjunction with Tcl version 8.6
#  Apr 21, 2020 01:06:04 PM CEST  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #ff00ff
set vTcl(analog_color_p) #00ff80
set vTcl(analog_color_m) #80ff00
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(pr,menufgcolor) #000000
set vTcl(pr,menubgcolor) #d9d9d9
set vTcl(pr,menuanalogcolor) #ececec
set vTcl(pr,treehighlight) #0000ff
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top58 {base} {
    global vTcl
    if {$base == ""} {
        set base .top58
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 966x728+485+150
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1055
    wm minsize $top 148 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    frame $top.fra61 \
        -borderwidth 2 -relief groove -background #000 -height 725 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 965 
    vTcl:DefineAlias "$top.fra61" "mainFrame" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra61
    frame $site_3_0.fra62 \
        -relief groove -background #000 -height 64 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 500 
    vTcl:DefineAlias "$site_3_0.fra62" "titleFrame" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.fra62
    label $site_4_0.lab63 \
        -activebackground #f9f9f9 -activeforeground black -background #000 \
        -disabledforeground #a3a3a3 -font {-family {Tw Cen MT} -size 23} \
        -foreground #fff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text {Méthode De dichotomie} 
    vTcl:DefineAlias "$site_4_0.lab63" "Label1" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.lab63 \
        -in $site_4_0 -x 0 -relx -0.02 -y 0 -rely 0.156 -width 0 \
        -relwidth 0.918 -height 0 -relheight 0.625 -anchor nw \
        -bordermode ignore 
    frame $site_3_0.fra64 \
        -relief groove -background #000 -height 204 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 793 
    vTcl:DefineAlias "$site_3_0.fra64" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.fra64
    entry $site_4_0.ent66 \
        -background #000 -disabledforeground #a3a3a3 \
        -font {-family {Tw Cen MT} -size 20} -foreground #00ff00 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -relief groove -selectbackground #c4c4c4 \
        -selectforeground black -width 584 
    vTcl:DefineAlias "$site_4_0.ent66" "entryFomule" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab67 \
        -activebackground #f9f9f9 -activeforeground black -background #000 \
        -disabledforeground #a3a3a3 -font {-family {Tw Cen MT} -size 20} \
        -foreground #fff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text {Entrez la formule :} 
    vTcl:DefineAlias "$site_4_0.lab67" "Label2" vTcl:WidgetProc "Toplevel1" 1
    button $site_4_0.but69 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #000 -disabledforeground #a3a3a3 \
        -font {-family {Tw Cen MT} -size 20} -foreground #fff \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -relief groove -text Solve 
    vTcl:DefineAlias "$site_4_0.but69" "btnSolve" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab73 \
        -activebackground #f9f9f9 -activeforeground black -background #000 \
        -disabledforeground #a3a3a3 \
        -font {-family {Yu Gothic UI Semibold} -size 24 -weight bold} \
        -foreground #fff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text {f(x) =} 
    vTcl:DefineAlias "$site_4_0.lab73" "Label2_10" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.ent66 \
        -in $site_4_0 -x 0 -relx 0.227 -y 0 -rely 0.294 -width 584 \
        -relwidth 0 -height 54 -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.lab67 \
        -in $site_4_0 -x 0 -relx 0.277 -y 0 -rely 0.049 -width 0 \
        -relwidth 0.405 -height 0 -relheight 0.152 -anchor nw \
        -bordermode ignore 
    place $site_4_0.but69 \
        -in $site_4_0 -x 0 -relx 0.296 -y 0 -rely 0.637 -width 276 \
        -relwidth 0 -height 53 -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.lab73 \
        -in $site_4_0 -x 0 -relx 0.076 -y 0 -rely 0.343 -width 0 \
        -relwidth 0.126 -height 0 -relheight 0.152 -anchor nw \
        -bordermode ignore 
    button $site_3_0.but70 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #b0b8ce -disabledforeground #a3a3a3 \
        -font {-family {Tw Cen MT} -size 20} -foreground #000 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -relief groove -text {Go Back} 
    vTcl:DefineAlias "$site_3_0.but70" "btnRetour" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.fra62 \
        -in $site_3_0 -x 0 -relx 0.487 -y 0 -width 0 -relwidth 0.518 \
        -height 0 -relheight 0.088 -anchor nw -bordermode ignore 
    place $site_3_0.fra64 \
        -in $site_3_0 -x 0 -relx 0.083 -y 0 -rely 0.082 -width 0 \
        -relwidth 0.821 -height 0 -relheight 0.28 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but70 \
        -in $site_3_0 -x 0 -relx 0.021 -y 0 -rely 0.014 -width 186 \
        -relwidth 0 -height 43 -relheight 0 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra61 \
        -in $top -x 0 -y 0 -width 0 -relwidth 1 -height 0 -relheight 1 \
        -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top58 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

