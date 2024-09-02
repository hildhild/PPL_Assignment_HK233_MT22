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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u01be\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"")
        buf.write("\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3")
        buf.write(")\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\7\61\u013a\n\61\f\61\16\61\u013d\13\61\3\62\3\62")
        buf.write("\3\62\5\62\u0142\n\62\3\62\7\62\u0145\n\62\f\62\16\62")
        buf.write("\u0148\13\62\5\62\u014a\n\62\3\63\3\63\7\63\u014e\n\63")
        buf.write("\f\63\16\63\u0151\13\63\3\64\3\64\5\64\u0155\n\64\3\64")
        buf.write("\6\64\u0158\n\64\r\64\16\64\u0159\3\65\3\65\3\65\3\66")
        buf.write("\3\66\3\66\5\66\u0162\n\66\3\66\3\66\3\66\3\66\3\66\3")
        buf.write("\66\5\66\u016a\n\66\3\66\3\66\3\67\3\67\3\67\3\67\5\67")
        buf.write("\u0172\n\67\38\38\38\39\39\79\u0179\n9\f9\169\u017c\13")
        buf.write("9\39\39\39\3:\3:\3:\3:\7:\u0185\n:\f:\16:\u0188\13:\3")
        buf.write(":\3:\3:\3:\3:\3;\3;\3;\3;\7;\u0193\n;\f;\16;\u0196\13")
        buf.write(";\3;\3;\3<\6<\u019b\n<\r<\16<\u019c\3<\3<\3=\3=\7=\u01a3")
        buf.write("\n=\f=\16=\u01a6\13=\3=\3=\3=\5=\u01ab\n=\3=\3=\3>\3>")
        buf.write("\3>\3?\3?\7?\u01b4\n?\f?\16?\u01b7\13?\3?\3?\3?\3@\3@")
        buf.write("\3@\3\u0186\2A\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#")
        buf.write("E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\2e\2g\2i\63k\64")
        buf.write("m\2o\2q\65s\66u\67w8y9{\2}:\177;\3\2\16\5\2C\\aac|\6\2")
        buf.write("\62;C\\aac|\3\2\63;\3\2\62;\4\2GGgg\4\2--//\6\2\f\f\16")
        buf.write("\17$$^^\t\2))^^ddhhppttvv\4\2\f\f\17\17\5\2\n\f\16\17")
        buf.write("\"\"\3\3\f\f\n\2$$))^^ddhhppttvv\2\u01ca\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2q\3\2\2\2\2s\3\2\2")
        buf.write("\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2}\3\2\2\2\2\177\3")
        buf.write("\2\2\2\3\u0081\3\2\2\2\5\u0086\3\2\2\2\7\u008c\3\2\2\2")
        buf.write("\t\u0094\3\2\2\2\13\u0097\3\2\2\2\r\u009c\3\2\2\2\17\u00a2")
        buf.write("\3\2\2\2\21\u00a8\3\2\2\2\23\u00ac\3\2\2\2\25\u00b5\3")
        buf.write("\2\2\2\27\u00b8\3\2\2\2\31\u00c0\3\2\2\2\33\u00c7\3\2")
        buf.write("\2\2\35\u00ce\3\2\2\2\37\u00d3\3\2\2\2!\u00d9\3\2\2\2")
        buf.write("#\u00de\3\2\2\2%\u00e2\3\2\2\2\'\u00eb\3\2\2\2)\u00ee")
        buf.write("\3\2\2\2+\u00f6\3\2\2\2-\u00fc\3\2\2\2/\u00fe\3\2\2\2")
        buf.write("\61\u0100\3\2\2\2\63\u0102\3\2\2\2\65\u0104\3\2\2\2\67")
        buf.write("\u0106\3\2\2\29\u0108\3\2\2\2;\u010b\3\2\2\2=\u010e\3")
        buf.write("\2\2\2?\u0111\3\2\2\2A\u0114\3\2\2\2C\u0116\3\2\2\2E\u0119")
        buf.write("\3\2\2\2G\u011b\3\2\2\2I\u011e\3\2\2\2K\u0121\3\2\2\2")
        buf.write("M\u0123\3\2\2\2O\u0125\3\2\2\2Q\u0127\3\2\2\2S\u0129\3")
        buf.write("\2\2\2U\u012b\3\2\2\2W\u012d\3\2\2\2Y\u012f\3\2\2\2[\u0131")
        buf.write("\3\2\2\2]\u0133\3\2\2\2_\u0135\3\2\2\2a\u0137\3\2\2\2")
        buf.write("c\u0149\3\2\2\2e\u014b\3\2\2\2g\u0152\3\2\2\2i\u015b\3")
        buf.write("\2\2\2k\u0169\3\2\2\2m\u0171\3\2\2\2o\u0173\3\2\2\2q\u0176")
        buf.write("\3\2\2\2s\u0180\3\2\2\2u\u018e\3\2\2\2w\u019a\3\2\2\2")
        buf.write("y\u01a0\3\2\2\2{\u01ae\3\2\2\2}\u01b1\3\2\2\2\177\u01bb")
        buf.write("\3\2\2\2\u0081\u0082\7c\2\2\u0082\u0083\7w\2\2\u0083\u0084")
        buf.write("\7v\2\2\u0084\u0085\7q\2\2\u0085\4\3\2\2\2\u0086\u0087")
        buf.write("\7d\2\2\u0087\u0088\7t\2\2\u0088\u0089\7g\2\2\u0089\u008a")
        buf.write("\7c\2\2\u008a\u008b\7m\2\2\u008b\6\3\2\2\2\u008c\u008d")
        buf.write("\7d\2\2\u008d\u008e\7q\2\2\u008e\u008f\7q\2\2\u008f\u0090")
        buf.write("\7n\2\2\u0090\u0091\7g\2\2\u0091\u0092\7c\2\2\u0092\u0093")
        buf.write("\7p\2\2\u0093\b\3\2\2\2\u0094\u0095\7f\2\2\u0095\u0096")
        buf.write("\7q\2\2\u0096\n\3\2\2\2\u0097\u0098\7g\2\2\u0098\u0099")
        buf.write("\7n\2\2\u0099\u009a\7u\2\2\u009a\u009b\7g\2\2\u009b\f")
        buf.write("\3\2\2\2\u009c\u009d\7h\2\2\u009d\u009e\7c\2\2\u009e\u009f")
        buf.write("\7n\2\2\u009f\u00a0\7u\2\2\u00a0\u00a1\7g\2\2\u00a1\16")
        buf.write("\3\2\2\2\u00a2\u00a3\7h\2\2\u00a3\u00a4\7n\2\2\u00a4\u00a5")
        buf.write("\7q\2\2\u00a5\u00a6\7c\2\2\u00a6\u00a7\7v\2\2\u00a7\20")
        buf.write("\3\2\2\2\u00a8\u00a9\7h\2\2\u00a9\u00aa\7q\2\2\u00aa\u00ab")
        buf.write("\7t\2\2\u00ab\22\3\2\2\2\u00ac\u00ad\7h\2\2\u00ad\u00ae")
        buf.write("\7w\2\2\u00ae\u00af\7p\2\2\u00af\u00b0\7e\2\2\u00b0\u00b1")
        buf.write("\7v\2\2\u00b1\u00b2\7k\2\2\u00b2\u00b3\7q\2\2\u00b3\u00b4")
        buf.write("\7p\2\2\u00b4\24\3\2\2\2\u00b5\u00b6\7k\2\2\u00b6\u00b7")
        buf.write("\7h\2\2\u00b7\26\3\2\2\2\u00b8\u00b9\7k\2\2\u00b9\u00ba")
        buf.write("\7p\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc\7g\2\2\u00bc\u00bd")
        buf.write("\7i\2\2\u00bd\u00be\7g\2\2\u00be\u00bf\7t\2\2\u00bf\30")
        buf.write("\3\2\2\2\u00c0\u00c1\7t\2\2\u00c1\u00c2\7g\2\2\u00c2\u00c3")
        buf.write("\7v\2\2\u00c3\u00c4\7w\2\2\u00c4\u00c5\7t\2\2\u00c5\u00c6")
        buf.write("\7p\2\2\u00c6\32\3\2\2\2\u00c7\u00c8\7u\2\2\u00c8\u00c9")
        buf.write("\7v\2\2\u00c9\u00ca\7t\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc")
        buf.write("\7p\2\2\u00cc\u00cd\7i\2\2\u00cd\34\3\2\2\2\u00ce\u00cf")
        buf.write("\7v\2\2\u00cf\u00d0\7t\2\2\u00d0\u00d1\7w\2\2\u00d1\u00d2")
        buf.write("\7g\2\2\u00d2\36\3\2\2\2\u00d3\u00d4\7y\2\2\u00d4\u00d5")
        buf.write("\7j\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7\7n\2\2\u00d7\u00d8")
        buf.write("\7g\2\2\u00d8 \3\2\2\2\u00d9\u00da\7x\2\2\u00da\u00db")
        buf.write("\7q\2\2\u00db\u00dc\7k\2\2\u00dc\u00dd\7f\2\2\u00dd\"")
        buf.write("\3\2\2\2\u00de\u00df\7q\2\2\u00df\u00e0\7w\2\2\u00e0\u00e1")
        buf.write("\7v\2\2\u00e1$\3\2\2\2\u00e2\u00e3\7e\2\2\u00e3\u00e4")
        buf.write("\7q\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6\7v\2\2\u00e6\u00e7")
        buf.write("\7k\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9\7w\2\2\u00e9\u00ea")
        buf.write("\7g\2\2\u00ea&\3\2\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed")
        buf.write("\7h\2\2\u00ed(\3\2\2\2\u00ee\u00ef\7k\2\2\u00ef\u00f0")
        buf.write("\7p\2\2\u00f0\u00f1\7j\2\2\u00f1\u00f2\7g\2\2\u00f2\u00f3")
        buf.write("\7t\2\2\u00f3\u00f4\7k\2\2\u00f4\u00f5\7v\2\2\u00f5*\3")
        buf.write("\2\2\2\u00f6\u00f7\7c\2\2\u00f7\u00f8\7t\2\2\u00f8\u00f9")
        buf.write("\7t\2\2\u00f9\u00fa\7c\2\2\u00fa\u00fb\7{\2\2\u00fb,\3")
        buf.write("\2\2\2\u00fc\u00fd\7-\2\2\u00fd.\3\2\2\2\u00fe\u00ff\7")
        buf.write("/\2\2\u00ff\60\3\2\2\2\u0100\u0101\7,\2\2\u0101\62\3\2")
        buf.write("\2\2\u0102\u0103\7\61\2\2\u0103\64\3\2\2\2\u0104\u0105")
        buf.write("\7\'\2\2\u0105\66\3\2\2\2\u0106\u0107\7#\2\2\u01078\3")
        buf.write("\2\2\2\u0108\u0109\7(\2\2\u0109\u010a\7(\2\2\u010a:\3")
        buf.write("\2\2\2\u010b\u010c\7~\2\2\u010c\u010d\7~\2\2\u010d<\3")
        buf.write("\2\2\2\u010e\u010f\7?\2\2\u010f\u0110\7?\2\2\u0110>\3")
        buf.write("\2\2\2\u0111\u0112\7#\2\2\u0112\u0113\7?\2\2\u0113@\3")
        buf.write("\2\2\2\u0114\u0115\7>\2\2\u0115B\3\2\2\2\u0116\u0117\7")
        buf.write(">\2\2\u0117\u0118\7?\2\2\u0118D\3\2\2\2\u0119\u011a\7")
        buf.write("@\2\2\u011aF\3\2\2\2\u011b\u011c\7@\2\2\u011c\u011d\7")
        buf.write("?\2\2\u011dH\3\2\2\2\u011e\u011f\7<\2\2\u011f\u0120\7")
        buf.write("<\2\2\u0120J\3\2\2\2\u0121\u0122\7*\2\2\u0122L\3\2\2\2")
        buf.write("\u0123\u0124\7+\2\2\u0124N\3\2\2\2\u0125\u0126\7]\2\2")
        buf.write("\u0126P\3\2\2\2\u0127\u0128\7_\2\2\u0128R\3\2\2\2\u0129")
        buf.write("\u012a\7\60\2\2\u012aT\3\2\2\2\u012b\u012c\7.\2\2\u012c")
        buf.write("V\3\2\2\2\u012d\u012e\7=\2\2\u012eX\3\2\2\2\u012f\u0130")
        buf.write("\7<\2\2\u0130Z\3\2\2\2\u0131\u0132\7}\2\2\u0132\\\3\2")
        buf.write("\2\2\u0133\u0134\7\177\2\2\u0134^\3\2\2\2\u0135\u0136")
        buf.write("\7?\2\2\u0136`\3\2\2\2\u0137\u013b\t\2\2\2\u0138\u013a")
        buf.write("\t\3\2\2\u0139\u0138\3\2\2\2\u013a\u013d\3\2\2\2\u013b")
        buf.write("\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013cb\3\2\2\2\u013d")
        buf.write("\u013b\3\2\2\2\u013e\u014a\7\62\2\2\u013f\u0146\t\4\2")
        buf.write("\2\u0140\u0142\7a\2\2\u0141\u0140\3\2\2\2\u0141\u0142")
        buf.write("\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0145\t\5\2\2\u0144")
        buf.write("\u0141\3\2\2\2\u0145\u0148\3\2\2\2\u0146\u0144\3\2\2\2")
        buf.write("\u0146\u0147\3\2\2\2\u0147\u014a\3\2\2\2\u0148\u0146\3")
        buf.write("\2\2\2\u0149\u013e\3\2\2\2\u0149\u013f\3\2\2\2\u014ad")
        buf.write("\3\2\2\2\u014b\u014f\5S*\2\u014c\u014e\t\5\2\2\u014d\u014c")
        buf.write("\3\2\2\2\u014e\u0151\3\2\2\2\u014f\u014d\3\2\2\2\u014f")
        buf.write("\u0150\3\2\2\2\u0150f\3\2\2\2\u0151\u014f\3\2\2\2\u0152")
        buf.write("\u0154\t\6\2\2\u0153\u0155\t\7\2\2\u0154\u0153\3\2\2\2")
        buf.write("\u0154\u0155\3\2\2\2\u0155\u0157\3\2\2\2\u0156\u0158\t")
        buf.write("\5\2\2\u0157\u0156\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u0157")
        buf.write("\3\2\2\2\u0159\u015a\3\2\2\2\u015ah\3\2\2\2\u015b\u015c")
        buf.write("\5c\62\2\u015c\u015d\b\65\2\2\u015dj\3\2\2\2\u015e\u015f")
        buf.write("\5c\62\2\u015f\u0161\5e\63\2\u0160\u0162\5g\64\2\u0161")
        buf.write("\u0160\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u016a\3\2\2\2")
        buf.write("\u0163\u0164\5e\63\2\u0164\u0165\5g\64\2\u0165\u016a\3")
        buf.write("\2\2\2\u0166\u0167\5c\62\2\u0167\u0168\5g\64\2\u0168\u016a")
        buf.write("\3\2\2\2\u0169\u015e\3\2\2\2\u0169\u0163\3\2\2\2\u0169")
        buf.write("\u0166\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016c\b\66\3")
        buf.write("\2\u016cl\3\2\2\2\u016d\u0172\n\b\2\2\u016e\u0172\5o8")
        buf.write("\2\u016f\u0170\7^\2\2\u0170\u0172\7$\2\2\u0171\u016d\3")
        buf.write("\2\2\2\u0171\u016e\3\2\2\2\u0171\u016f\3\2\2\2\u0172n")
        buf.write("\3\2\2\2\u0173\u0174\7^\2\2\u0174\u0175\t\t\2\2\u0175")
        buf.write("p\3\2\2\2\u0176\u017a\7$\2\2\u0177\u0179\5m\67\2\u0178")
        buf.write("\u0177\3\2\2\2\u0179\u017c\3\2\2\2\u017a\u0178\3\2\2\2")
        buf.write("\u017a\u017b\3\2\2\2\u017b\u017d\3\2\2\2\u017c\u017a\3")
        buf.write("\2\2\2\u017d\u017e\7$\2\2\u017e\u017f\b9\4\2\u017fr\3")
        buf.write("\2\2\2\u0180\u0181\7\61\2\2\u0181\u0182\7,\2\2\u0182\u0186")
        buf.write("\3\2\2\2\u0183\u0185\13\2\2\2\u0184\u0183\3\2\2\2\u0185")
        buf.write("\u0188\3\2\2\2\u0186\u0187\3\2\2\2\u0186\u0184\3\2\2\2")
        buf.write("\u0187\u0189\3\2\2\2\u0188\u0186\3\2\2\2\u0189\u018a\7")
        buf.write(",\2\2\u018a\u018b\7\61\2\2\u018b\u018c\3\2\2\2\u018c\u018d")
        buf.write("\b:\5\2\u018dt\3\2\2\2\u018e\u018f\7\61\2\2\u018f\u0190")
        buf.write("\7\61\2\2\u0190\u0194\3\2\2\2\u0191\u0193\n\n\2\2\u0192")
        buf.write("\u0191\3\2\2\2\u0193\u0196\3\2\2\2\u0194\u0192\3\2\2\2")
        buf.write("\u0194\u0195\3\2\2\2\u0195\u0197\3\2\2\2\u0196\u0194\3")
        buf.write("\2\2\2\u0197\u0198\b;\5\2\u0198v\3\2\2\2\u0199\u019b\t")
        buf.write("\13\2\2\u019a\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019c")
        buf.write("\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019e\3\2\2\2")
        buf.write("\u019e\u019f\b<\5\2\u019fx\3\2\2\2\u01a0\u01a4\7$\2\2")
        buf.write("\u01a1\u01a3\5m\67\2\u01a2\u01a1\3\2\2\2\u01a3\u01a6\3")
        buf.write("\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01aa")
        buf.write("\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a7\u01ab\t\f\2\2\u01a8")
        buf.write("\u01a9\7\17\2\2\u01a9\u01ab\7\f\2\2\u01aa\u01a7\3\2\2")
        buf.write("\2\u01aa\u01a8\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01ad")
        buf.write("\b=\6\2\u01adz\3\2\2\2\u01ae\u01af\7^\2\2\u01af\u01b0")
        buf.write("\n\r\2\2\u01b0|\3\2\2\2\u01b1\u01b5\7$\2\2\u01b2\u01b4")
        buf.write("\5m\67\2\u01b3\u01b2\3\2\2\2\u01b4\u01b7\3\2\2\2\u01b5")
        buf.write("\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b8\3\2\2\2")
        buf.write("\u01b7\u01b5\3\2\2\2\u01b8\u01b9\5{>\2\u01b9\u01ba\b?")
        buf.write("\7\2\u01ba~\3\2\2\2\u01bb\u01bc\13\2\2\2\u01bc\u01bd\b")
        buf.write("@\b\2\u01bd\u0080\3\2\2\2\24\2\u013b\u0141\u0146\u0149")
        buf.write("\u014f\u0154\u0159\u0161\u0169\u0171\u017a\u0186\u0194")
        buf.write("\u019c\u01a4\u01aa\u01b5\t\3\65\2\3\66\3\39\4\b\2\2\3")
        buf.write("=\5\3?\6\3@\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AUTO = 1
    BREAK = 2
    BOOLEAN = 3
    DO = 4
    ELSE = 5
    FALSE = 6
    FLOAT = 7
    FOR = 8
    FUNCTION = 9
    IF = 10
    INTEGER = 11
    RETURN = 12
    STRING = 13
    TRUE = 14
    WHILE = 15
    VOID = 16
    OUT = 17
    CONTINUE = 18
    OF = 19
    INHERIT = 20
    ARRAY = 21
    ADD = 22
    SUB = 23
    MUL = 24
    DIV = 25
    MOD = 26
    NOT = 27
    AND = 28
    OR = 29
    EQUAL = 30
    DIFF = 31
    LT = 32
    LTE = 33
    GT = 34
    GTE = 35
    CONCAT = 36
    LP = 37
    RP = 38
    LSB = 39
    RSB = 40
    POINT = 41
    COMMA = 42
    SEMI = 43
    COLON = 44
    LCB = 45
    RCB = 46
    ASSIGN = 47
    ID = 48
    INT_LIT = 49
    FLOAT_LIT = 50
    STR_LIT = 51
    COMMENT = 52
    INLINE_COMMENT = 53
    WS = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56
    ERROR_CHAR = 57

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
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
            "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "TRUE", 
            "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
            "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", 
            "DIFF", "LT", "LTE", "GT", "GTE", "CONCAT", "LP", "RP", "LSB", 
            "RSB", "POINT", "COMMA", "SEMI", "COLON", "LCB", "RCB", "ASSIGN", 
            "ID", "INT_LIT", "FLOAT_LIT", "STR_LIT", "COMMENT", "INLINE_COMMENT", 
            "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
                  "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
                  "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
                  "ARRAY", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", 
                  "OR", "EQUAL", "DIFF", "LT", "LTE", "GT", "GTE", "CONCAT", 
                  "LP", "RP", "LSB", "RSB", "POINT", "COMMA", "SEMI", "COLON", 
                  "LCB", "RCB", "ASSIGN", "ID", "INT_PART", "DEC_PART", 
                  "EXP_PART", "INT_LIT", "FLOAT_LIT", "STR_CHAR", "ESC_SEQ", 
                  "STR_LIT", "COMMENT", "INLINE_COMMENT", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESC", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[51] = self.INT_LIT_action 
            actions[52] = self.FLOAT_LIT_action 
            actions[55] = self.STR_LIT_action 
            actions[59] = self.UNCLOSE_STRING_action 
            actions[61] = self.ILLEGAL_ESCAPE_action 
            actions[62] = self.ERROR_CHAR_action 
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
     


