from pymol import cmd


def coloraf(selection="all"):

    """
    AUTHOR
    Christian Balbin

    DESCRIPTION
    Colors Alphafold structures by pLDDT

    USAGE
    coloraf sele

    PARAMETERS

    sele (string)
    The name of the selection/object to color by pLDDT. Default: all
    """

    # Define custom colors from hex, closer to AF coloring system
    cmd.set_color("af_blue", hex_to_rgb("#106DFF"))
    cmd.set_color("af_cyan", hex_to_rgb("#10CFF1"))
    cmd.set_color("af_yellow", hex_to_rgb("#F6ED12"))
    cmd.set_color("af_orange", hex_to_rgb("#EF821E"))

    # Modified cutoff values so they won't be ignored
    cmd.color("af_blue",   f"({selection}) and b > 89.999")
    cmd.color("af_cyan",   f"({selection}) and b < 90 and b > 69.999")
    cmd.color("af_yellow", f"({selection}) and b < 70 and b > 49.999")
    cmd.color("af_orange", f"({selection}) and b < 50")


cmd.extend("coloraf", coloraf)
cmd.auto_arg[0]["coloraf"] = [cmd.object_sc, "object", ""]
