

import java.io.*;
import java.io.IOException;

//import bkool.codegeneration.IllegalRuntimeException;


public class io {
	
	public static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	public static Writer writer = new BufferedWriter(new OutputStreamWriter(System.out));
	
	// truncate the given floating-point number to an integer.
	public static int int_of_float(float a) {
	    return (int) a;
        }
	// convert an integer to floating-point
	public static float float_to_int(int a) {
            return (float) a;
        }
        //convert the given string to an integer.
	public static int int_of_string(String a) {
 	    return Integer.parseInt(a);
	}
        // return the string representation of an integer, in decimal
	public static String string_of_int(int a) {
	    return Integer.toString(a);
	}
	// convert the given string to a float.
	public static float float_of_string(String a) {
	    return Float.parseFloat(a);
	}
	// convert the given string to a boolean
	public static String string_of_float(float a) {
	    return Float.toString(a);
	}
	// convert the given string to a boolean
	public static boolean bool_of_string(String a) {
	    return Boolean.parseBoolean(a);
	}
	// convert a boolean to string
	public static String string_of_bool(boolean a) {
	    return Boolean.toString(a);
	}

    /** reads and returns a string value from the standard input
     *  @return int a string value read from standard input
     */
    public static String read() {
        String tmp = "";
        try {
            tmp = input.readLine();
            return tmp;
        } catch (IOException e) {
        	e.printStackTrace();
        }
        return tmp;
    }

    /** prints the value of the string to the standard output
     *	@param a the string is printed out
     */
     public static void print(String a ) {
    	 System.out.print(a);
    }
    
    /** same as putString except that it also prints a new line
     *	@param a the string is printed out
     */
    public static void printStrLn(String a)  {
    	System.out.println(a);
    }
    /** print out an empty line
     **/
    public static void printLn()  {
    	System.out.println();
    }
    
    /**
	 * reads and returns an integer value from the standard input
	 * 
	 * @return int an integer number read from standard input
	 */
	public static int readInteger() {
		String tmp = "";
		try {
			tmp = input.readLine();
			return Integer.parseInt(tmp);
		} catch (IOException e) {
			e.printStackTrace();
		} catch (NumberFormatException e) {
			e.printStackTrace();
		}
		return 0;
	}

	/**
	 * print out the value of the integer i to the standard output
	 * 
	 * @param i the value is printed out
	 */
	public static void printInteger(int i) {

		System.out.print(i + "");

	}
	/**
	 * return a floating-point value read from the standard input
	 * 
	 * @return float the floating-point value
	 */
	public static float readFloat() {
		String tmp = "";
		try {
			tmp = input.readLine();
			return Float.parseFloat(tmp);
		} catch (IOException e) {
			e.printStackTrace();
			;
		} catch (NumberFormatException e) {
			e.printStackTrace();
			;
		}
		return 0.0F;
	}

	/**
	 * print out the value of the float f to the standard output
	 * 
	 * @param f the floating-point value is printed out
	 */
	public static void writeFloat(float f) {
		System.out.print(f + "");
	}

	/**
	 * reads and returns a boolean value from the standard input
	 * 
	 * @return int a boolean value read from standard input
	 */
	public static boolean readBoolean() {
		String tmp = "";
		try {
			tmp = input.readLine();
			if (tmp.equalsIgnoreCase("true"))
				return true;
			else // if (tmp.equalsIgnoreCase("false"))
				return false;
			// else throw new IllegalRuntimeException(tmp);
		} catch (IOException e) {
			e.printStackTrace();
		}
		return false;
	}

	/**
	 * print out the value of the boolean b to the standard output
	 * 
	 * @param b the boolean value is printed out
	 */
	public static void printBoolean(boolean b) {
		System.out.print(b + "");
	}

	/**
	 * reads and returns a string value from the standard input
	 * 
	 * @return int a string value read from standard input
	 */
	public static String readString() {
		String tmp = "";
		try {
			tmp = input.readLine();
			return tmp;
		} catch (IOException e) {
			e.printStackTrace();
		}
		return tmp;
	}

	/**
	 * prints the value of the string to the standard output
	 * 
	 * @param a the string is printed out
	 */
	public static void printString(String a) {
		System.out.print(a);
	}

	public static void close() {
		try {
			writer.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}

