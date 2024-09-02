# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u01c4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\5\2")
        buf.write("\u0086\n\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3")
        buf.write("%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3")
        buf.write("-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\7\62\u0140")
        buf.write("\n\62\f\62\16\62\u0143\13\62\3\63\3\63\3\63\5\63\u0148")
        buf.write("\n\63\3\63\7\63\u014b\n\63\f\63\16\63\u014e\13\63\5\63")
        buf.write("\u0150\n\63\3\64\3\64\7\64\u0154\n\64\f\64\16\64\u0157")
        buf.write("\13\64\3\65\3\65\5\65\u015b\n\65\3\65\6\65\u015e\n\65")
        buf.write("\r\65\16\65\u015f\3\66\3\66\3\66\3\67\3\67\3\67\5\67\u0168")
        buf.write("\n\67\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u0170\n\67\3")
        buf.write("\67\3\67\38\38\38\38\58\u0178\n8\39\39\39\3:\3:\7:\u017f")
        buf.write("\n:\f:\16:\u0182\13:\3:\3:\3:\3;\3;\3;\3;\7;\u018b\n;")
        buf.write("\f;\16;\u018e\13;\3;\3;\3;\3;\3;\3<\3<\3<\3<\7<\u0199")
        buf.write("\n<\f<\16<\u019c\13<\3<\3<\3=\6=\u01a1\n=\r=\16=\u01a2")
        buf.write("\3=\3=\3>\3>\7>\u01a9\n>\f>\16>\u01ac\13>\3>\3>\3>\5>")
        buf.write("\u01b1\n>\3>\3>\3?\3?\3?\3@\3@\7@\u01ba\n@\f@\16@\u01bd")
        buf.write("\13@\3@\3@\3@\3A\3A\3A\3\u018c\2B\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\2g\2i\2k\64m\65o\2q\2s\66u\67w8y9{:}\2\177;")
        buf.write("\u0081<\3\2\16\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62")
        buf.write(";\4\2GGgg\4\2--//\6\2\f\f\16\17$$^^\t\2))^^ddhhppttvv")
        buf.write("\4\2\f\f\17\17\5\2\n\f\16\17\"\"\3\3\f\f\n\2$$))^^ddh")
        buf.write("hppttvv\2\u01d1\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2k\3\2\2\2\2m\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2")
        buf.write("\2\2y\3\2\2\2\2{\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2")
        buf.write("\3\u0085\3\2\2\2\5\u0087\3\2\2\2\7\u008c\3\2\2\2\t\u0092")
        buf.write("\3\2\2\2\13\u009a\3\2\2\2\r\u009d\3\2\2\2\17\u00a2\3\2")
        buf.write("\2\2\21\u00a8\3\2\2\2\23\u00ae\3\2\2\2\25\u00b2\3\2\2")
        buf.write("\2\27\u00bb\3\2\2\2\31\u00be\3\2\2\2\33\u00c6\3\2\2\2")
        buf.write("\35\u00cd\3\2\2\2\37\u00d4\3\2\2\2!\u00d9\3\2\2\2#\u00df")
        buf.write("\3\2\2\2%\u00e4\3\2\2\2\'\u00e8\3\2\2\2)\u00f1\3\2\2\2")
        buf.write("+\u00f4\3\2\2\2-\u00fc\3\2\2\2/\u0102\3\2\2\2\61\u0104")
        buf.write("\3\2\2\2\63\u0106\3\2\2\2\65\u0108\3\2\2\2\67\u010a\3")
        buf.write("\2\2\29\u010c\3\2\2\2;\u010e\3\2\2\2=\u0111\3\2\2\2?\u0114")
        buf.write("\3\2\2\2A\u0117\3\2\2\2C\u011a\3\2\2\2E\u011c\3\2\2\2")
        buf.write("G\u011f\3\2\2\2I\u0121\3\2\2\2K\u0124\3\2\2\2M\u0127\3")
        buf.write("\2\2\2O\u0129\3\2\2\2Q\u012b\3\2\2\2S\u012d\3\2\2\2U\u012f")
        buf.write("\3\2\2\2W\u0131\3\2\2\2Y\u0133\3\2\2\2[\u0135\3\2\2\2")
        buf.write("]\u0137\3\2\2\2_\u0139\3\2\2\2a\u013b\3\2\2\2c\u013d\3")
        buf.write("\2\2\2e\u014f\3\2\2\2g\u0151\3\2\2\2i\u0158\3\2\2\2k\u0161")
        buf.write("\3\2\2\2m\u016f\3\2\2\2o\u0177\3\2\2\2q\u0179\3\2\2\2")
        buf.write("s\u017c\3\2\2\2u\u0186\3\2\2\2w\u0194\3\2\2\2y\u01a0\3")
        buf.write("\2\2\2{\u01a6\3\2\2\2}\u01b4\3\2\2\2\177\u01b7\3\2\2\2")
        buf.write("\u0081\u01c1\3\2\2\2\u0083\u0086\5\37\20\2\u0084\u0086")
        buf.write("\5\17\b\2\u0085\u0083\3\2\2\2\u0085\u0084\3\2\2\2\u0086")
        buf.write("\4\3\2\2\2\u0087\u0088\7c\2\2\u0088\u0089\7w\2\2\u0089")
        buf.write("\u008a\7v\2\2\u008a\u008b\7q\2\2\u008b\6\3\2\2\2\u008c")
        buf.write("\u008d\7d\2\2\u008d\u008e\7t\2\2\u008e\u008f\7g\2\2\u008f")
        buf.write("\u0090\7c\2\2\u0090\u0091\7m\2\2\u0091\b\3\2\2\2\u0092")
        buf.write("\u0093\7d\2\2\u0093\u0094\7q\2\2\u0094\u0095\7q\2\2\u0095")
        buf.write("\u0096\7n\2\2\u0096\u0097\7g\2\2\u0097\u0098\7c\2\2\u0098")
        buf.write("\u0099\7p\2\2\u0099\n\3\2\2\2\u009a\u009b\7f\2\2\u009b")
        buf.write("\u009c\7q\2\2\u009c\f\3\2\2\2\u009d\u009e\7g\2\2\u009e")
        buf.write("\u009f\7n\2\2\u009f\u00a0\7u\2\2\u00a0\u00a1\7g\2\2\u00a1")
        buf.write("\16\3\2\2\2\u00a2\u00a3\7h\2\2\u00a3\u00a4\7c\2\2\u00a4")
        buf.write("\u00a5\7n\2\2\u00a5\u00a6\7u\2\2\u00a6\u00a7\7g\2\2\u00a7")
        buf.write("\20\3\2\2\2\u00a8\u00a9\7h\2\2\u00a9\u00aa\7n\2\2\u00aa")
        buf.write("\u00ab\7q\2\2\u00ab\u00ac\7c\2\2\u00ac\u00ad\7v\2\2\u00ad")
        buf.write("\22\3\2\2\2\u00ae\u00af\7h\2\2\u00af\u00b0\7q\2\2\u00b0")
        buf.write("\u00b1\7t\2\2\u00b1\24\3\2\2\2\u00b2\u00b3\7h\2\2\u00b3")
        buf.write("\u00b4\7w\2\2\u00b4\u00b5\7p\2\2\u00b5\u00b6\7e\2\2\u00b6")
        buf.write("\u00b7\7v\2\2\u00b7\u00b8\7k\2\2\u00b8\u00b9\7q\2\2\u00b9")
        buf.write("\u00ba\7p\2\2\u00ba\26\3\2\2\2\u00bb\u00bc\7k\2\2\u00bc")
        buf.write("\u00bd\7h\2\2\u00bd\30\3\2\2\2\u00be\u00bf\7k\2\2\u00bf")
        buf.write("\u00c0\7p\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2\7g\2\2\u00c2")
        buf.write("\u00c3\7i\2\2\u00c3\u00c4\7g\2\2\u00c4\u00c5\7t\2\2\u00c5")
        buf.write("\32\3\2\2\2\u00c6\u00c7\7t\2\2\u00c7\u00c8\7g\2\2\u00c8")
        buf.write("\u00c9\7v\2\2\u00c9\u00ca\7w\2\2\u00ca\u00cb\7t\2\2\u00cb")
        buf.write("\u00cc\7p\2\2\u00cc\34\3\2\2\2\u00cd\u00ce\7u\2\2\u00ce")
        buf.write("\u00cf\7v\2\2\u00cf\u00d0\7t\2\2\u00d0\u00d1\7k\2\2\u00d1")
        buf.write("\u00d2\7p\2\2\u00d2\u00d3\7i\2\2\u00d3\36\3\2\2\2\u00d4")
        buf.write("\u00d5\7v\2\2\u00d5\u00d6\7t\2\2\u00d6\u00d7\7w\2\2\u00d7")
        buf.write("\u00d8\7g\2\2\u00d8 \3\2\2\2\u00d9\u00da\7y\2\2\u00da")
        buf.write("\u00db\7j\2\2\u00db\u00dc\7k\2\2\u00dc\u00dd\7n\2\2\u00dd")
        buf.write("\u00de\7g\2\2\u00de\"\3\2\2\2\u00df\u00e0\7x\2\2\u00e0")
        buf.write("\u00e1\7q\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3\7f\2\2\u00e3")
        buf.write("$\3\2\2\2\u00e4\u00e5\7q\2\2\u00e5\u00e6\7w\2\2\u00e6")
        buf.write("\u00e7\7v\2\2\u00e7&\3\2\2\2\u00e8\u00e9\7e\2\2\u00e9")
        buf.write("\u00ea\7q\2\2\u00ea\u00eb\7p\2\2\u00eb\u00ec\7v\2\2\u00ec")
        buf.write("\u00ed\7k\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef\7w\2\2\u00ef")
        buf.write("\u00f0\7g\2\2\u00f0(\3\2\2\2\u00f1\u00f2\7q\2\2\u00f2")
        buf.write("\u00f3\7h\2\2\u00f3*\3\2\2\2\u00f4\u00f5\7k\2\2\u00f5")
        buf.write("\u00f6\7p\2\2\u00f6\u00f7\7j\2\2\u00f7\u00f8\7g\2\2\u00f8")
        buf.write("\u00f9\7t\2\2\u00f9\u00fa\7k\2\2\u00fa\u00fb\7v\2\2\u00fb")
        buf.write(",\3\2\2\2\u00fc\u00fd\7c\2\2\u00fd\u00fe\7t\2\2\u00fe")
        buf.write("\u00ff\7t\2\2\u00ff\u0100\7c\2\2\u0100\u0101\7{\2\2\u0101")
        buf.write(".\3\2\2\2\u0102\u0103\7-\2\2\u0103\60\3\2\2\2\u0104\u0105")
        buf.write("\7/\2\2\u0105\62\3\2\2\2\u0106\u0107\7,\2\2\u0107\64\3")
        buf.write("\2\2\2\u0108\u0109\7\61\2\2\u0109\66\3\2\2\2\u010a\u010b")
        buf.write("\7\'\2\2\u010b8\3\2\2\2\u010c\u010d\7#\2\2\u010d:\3\2")
        buf.write("\2\2\u010e\u010f\7(\2\2\u010f\u0110\7(\2\2\u0110<\3\2")
        buf.write("\2\2\u0111\u0112\7~\2\2\u0112\u0113\7~\2\2\u0113>\3\2")
        buf.write("\2\2\u0114\u0115\7?\2\2\u0115\u0116\7?\2\2\u0116@\3\2")
        buf.write("\2\2\u0117\u0118\7#\2\2\u0118\u0119\7?\2\2\u0119B\3\2")
        buf.write("\2\2\u011a\u011b\7>\2\2\u011bD\3\2\2\2\u011c\u011d\7>")
        buf.write("\2\2\u011d\u011e\7?\2\2\u011eF\3\2\2\2\u011f\u0120\7@")
        buf.write("\2\2\u0120H\3\2\2\2\u0121\u0122\7@\2\2\u0122\u0123\7?")
        buf.write("\2\2\u0123J\3\2\2\2\u0124\u0125\7<\2\2\u0125\u0126\7<")
        buf.write("\2\2\u0126L\3\2\2\2\u0127\u0128\7*\2\2\u0128N\3\2\2\2")
        buf.write("\u0129\u012a\7+\2\2\u012aP\3\2\2\2\u012b\u012c\7]\2\2")
        buf.write("\u012cR\3\2\2\2\u012d\u012e\7_\2\2\u012eT\3\2\2\2\u012f")
        buf.write("\u0130\7\60\2\2\u0130V\3\2\2\2\u0131\u0132\7.\2\2\u0132")
        buf.write("X\3\2\2\2\u0133\u0134\7=\2\2\u0134Z\3\2\2\2\u0135\u0136")
        buf.write("\7<\2\2\u0136\\\3\2\2\2\u0137\u0138\7}\2\2\u0138^\3\2")
        buf.write("\2\2\u0139\u013a\7\177\2\2\u013a`\3\2\2\2\u013b\u013c")
        buf.write("\7?\2\2\u013cb\3\2\2\2\u013d\u0141\t\2\2\2\u013e\u0140")
        buf.write("\t\3\2\2\u013f\u013e\3\2\2\2\u0140\u0143\3\2\2\2\u0141")
        buf.write("\u013f\3\2\2\2\u0141\u0142\3\2\2\2\u0142d\3\2\2\2\u0143")
        buf.write("\u0141\3\2\2\2\u0144\u0150\7\62\2\2\u0145\u014c\t\4\2")
        buf.write("\2\u0146\u0148\7a\2\2\u0147\u0146\3\2\2\2\u0147\u0148")
        buf.write("\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014b\t\5\2\2\u014a")
        buf.write("\u0147\3\2\2\2\u014b\u014e\3\2\2\2\u014c\u014a\3\2\2\2")
        buf.write("\u014c\u014d\3\2\2\2\u014d\u0150\3\2\2\2\u014e\u014c\3")
        buf.write("\2\2\2\u014f\u0144\3\2\2\2\u014f\u0145\3\2\2\2\u0150f")
        buf.write("\3\2\2\2\u0151\u0155\5U+\2\u0152\u0154\t\5\2\2\u0153\u0152")
        buf.write("\3\2\2\2\u0154\u0157\3\2\2\2\u0155\u0153\3\2\2\2\u0155")
        buf.write("\u0156\3\2\2\2\u0156h\3\2\2\2\u0157\u0155\3\2\2\2\u0158")
        buf.write("\u015a\t\6\2\2\u0159\u015b\t\7\2\2\u015a\u0159\3\2\2\2")
        buf.write("\u015a\u015b\3\2\2\2\u015b\u015d\3\2\2\2\u015c\u015e\t")
        buf.write("\5\2\2\u015d\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u015d")
        buf.write("\3\2\2\2\u015f\u0160\3\2\2\2\u0160j\3\2\2\2\u0161\u0162")
        buf.write("\5e\63\2\u0162\u0163\b\66\2\2\u0163l\3\2\2\2\u0164\u0165")
        buf.write("\5e\63\2\u0165\u0167\5g\64\2\u0166\u0168\5i\65\2\u0167")
        buf.write("\u0166\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u0170\3\2\2\2")
        buf.write("\u0169\u016a\5g\64\2\u016a\u016b\5i\65\2\u016b\u0170\3")
        buf.write("\2\2\2\u016c\u016d\5e\63\2\u016d\u016e\5i\65\2\u016e\u0170")
        buf.write("\3\2\2\2\u016f\u0164\3\2\2\2\u016f\u0169\3\2\2\2\u016f")
        buf.write("\u016c\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0172\b\67\3")
        buf.write("\2\u0172n\3\2\2\2\u0173\u0178\n\b\2\2\u0174\u0178\5q9")
        buf.write("\2\u0175\u0176\7^\2\2\u0176\u0178\7$\2\2\u0177\u0173\3")
        buf.write("\2\2\2\u0177\u0174\3\2\2\2\u0177\u0175\3\2\2\2\u0178p")
        buf.write("\3\2\2\2\u0179\u017a\7^\2\2\u017a\u017b\t\t\2\2\u017b")
        buf.write("r\3\2\2\2\u017c\u0180\7$\2\2\u017d\u017f\5o8\2\u017e\u017d")
        buf.write("\3\2\2\2\u017f\u0182\3\2\2\2\u0180\u017e\3\2\2\2\u0180")
        buf.write("\u0181\3\2\2\2\u0181\u0183\3\2\2\2\u0182\u0180\3\2\2\2")
        buf.write("\u0183\u0184\7$\2\2\u0184\u0185\b:\4\2\u0185t\3\2\2\2")
        buf.write("\u0186\u0187\7\61\2\2\u0187\u0188\7,\2\2\u0188\u018c\3")
        buf.write("\2\2\2\u0189\u018b\13\2\2\2\u018a\u0189\3\2\2\2\u018b")
        buf.write("\u018e\3\2\2\2\u018c\u018d\3\2\2\2\u018c\u018a\3\2\2\2")
        buf.write("\u018d\u018f\3\2\2\2\u018e\u018c\3\2\2\2\u018f\u0190\7")
        buf.write(",\2\2\u0190\u0191\7\61\2\2\u0191\u0192\3\2\2\2\u0192\u0193")
        buf.write("\b;\5\2\u0193v\3\2\2\2\u0194\u0195\7\61\2\2\u0195\u0196")
        buf.write("\7\61\2\2\u0196\u019a\3\2\2\2\u0197\u0199\n\n\2\2\u0198")
        buf.write("\u0197\3\2\2\2\u0199\u019c\3\2\2\2\u019a\u0198\3\2\2\2")
        buf.write("\u019a\u019b\3\2\2\2\u019b\u019d\3\2\2\2\u019c\u019a\3")
        buf.write("\2\2\2\u019d\u019e\b<\5\2\u019ex\3\2\2\2\u019f\u01a1\t")
        buf.write("\13\2\2\u01a0\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2")
        buf.write("\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a4\3\2\2\2")
        buf.write("\u01a4\u01a5\b=\5\2\u01a5z\3\2\2\2\u01a6\u01aa\7$\2\2")
        buf.write("\u01a7\u01a9\5o8\2\u01a8\u01a7\3\2\2\2\u01a9\u01ac\3\2")
        buf.write("\2\2\u01aa\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01b0")
        buf.write("\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ad\u01b1\t\f\2\2\u01ae")
        buf.write("\u01af\7\17\2\2\u01af\u01b1\7\f\2\2\u01b0\u01ad\3\2\2")
        buf.write("\2\u01b0\u01ae\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b3")
        buf.write("\b>\6\2\u01b3|\3\2\2\2\u01b4\u01b5\7^\2\2\u01b5\u01b6")
        buf.write("\n\r\2\2\u01b6~\3\2\2\2\u01b7\u01bb\7$\2\2\u01b8\u01ba")
        buf.write("\5o8\2\u01b9\u01b8\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01b9")
        buf.write("\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01be\3\2\2\2\u01bd")
        buf.write("\u01bb\3\2\2\2\u01be\u01bf\5}?\2\u01bf\u01c0\b@\7\2\u01c0")
        buf.write("\u0080\3\2\2\2\u01c1\u01c2\13\2\2\2\u01c2\u01c3\bA\b\2")
        buf.write("\u01c3\u0082\3\2\2\2\25\2\u0085\u0141\u0147\u014c\u014f")
        buf.write("\u0155\u015a\u015f\u0167\u016f\u0177\u0180\u018c\u019a")
        buf.write("\u01a2\u01aa\u01b0\u01bb\t\3\66\2\3\67\3\3:\4\b\2\2\3")
        buf.write(">\5\3@\6\3A\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOL_LIT = 1
    AUTO = 2
    BREAK = 3
    BOOLEAN = 4
    DO = 5
    ELSE = 6
    FALSE = 7
    FLOAT = 8
    FOR = 9
    FUNCTION = 10
    IF = 11
    INTEGER = 12
    RETURN = 13
    STRING = 14
    TRUE = 15
    WHILE = 16
    VOID = 17
    OUT = 18
    CONTINUE = 19
    OF = 20
    INHERIT = 21
    ARRAY = 22
    ADD = 23
    SUB = 24
    MUL = 25
    DIV = 26
    MOD = 27
    NOT = 28
    AND = 29
    OR = 30
    EQUAL = 31
    DIFF = 32
    LT = 33
    LTE = 34
    GT = 35
    GTE = 36
    CONCAT = 37
    LP = 38
    RP = 39
    LSB = 40
    RSB = 41
    POINT = 42
    COMMA = 43
    SEMI = 44
    COLON = 45
    LCB = 46
    RCB = 47
    ASSIGN = 48
    ID = 49
    INT_LIT = 50
    FLOAT_LIT = 51
    STR_LIT = 52
    COMMENT = 53
    INLINE_COMMENT = 54
    WS = 55
    UNCLOSE_STRING = 56
    ILLEGAL_ESCAPE = 57
    ERROR_CHAR = 58

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'true'", "'while'", "'void'", "'out'", "'continue'", 
            "'of'", "'inherit'", "'array'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'::'", "'('", "')'", "'['", "']'", "'.'", "','", 
            "';'", "':'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "BOOL_LIT", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", 
            "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
            "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
            "ARRAY", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
            "EQUAL", "DIFF", "LT", "LTE", "GT", "GTE", "CONCAT", "LP", "RP", 
            "LSB", "RSB", "POINT", "COMMA", "SEMI", "COLON", "LCB", "RCB", 
            "ASSIGN", "ID", "INT_LIT", "FLOAT_LIT", "STR_LIT", "COMMENT", 
            "INLINE_COMMENT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "BOOL_LIT", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", 
                  "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
                  "RETURN", "STRING", "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", 
                  "OF", "INHERIT", "ARRAY", "ADD", "SUB", "MUL", "DIV", 
                  "MOD", "NOT", "AND", "OR", "EQUAL", "DIFF", "LT", "LTE", 
                  "GT", "GTE", "CONCAT", "LP", "RP", "LSB", "RSB", "POINT", 
                  "COMMA", "SEMI", "COLON", "LCB", "RCB", "ASSIGN", "ID", 
                  "INT_PART", "DEC_PART", "EXP_PART", "INT_LIT", "FLOAT_LIT", 
                  "STR_CHAR", "ESC_SEQ", "STR_LIT", "COMMENT", "INLINE_COMMENT", 
                  "WS", "UNCLOSE_STRING", "ILLEGAL_ESC", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[52] = self.INT_LIT_action 
            actions[53] = self.FLOAT_LIT_action 
            actions[56] = self.STR_LIT_action 
            actions[60] = self.UNCLOSE_STRING_action 
            actions[62] = self.ILLEGAL_ESCAPE_action 
            actions[63] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_', '')
     

    def FLOAT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_', '')
     

    def STR_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            if self.text[-1] == '\n':
            	if self.text[-2] == '\r':
            		raise UncloseString(self.text[1:-2]);
            	else:
            		raise UncloseString(self.text[1:-1]);
            else:
            	raise UncloseString(self.text[1:]);

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise IllegalEscape(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


