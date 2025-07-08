import javax.crypto.Cipher;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.BadPaddingException;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;
import java.util.Scanner;

// BEGIN SOLUTION
// Please import only standard libraries and make sure that your code compiles and runs without unhandled exceptions 
// END SOLUTION
 
public class HW2_Vemireddy {    

  static void P1() throws Exception {
    byte[] cipherBMP = Files.readAllBytes(Paths.get("cipher1.bmp"));
    
    // BEGIN SOLUTION
    byte[] iv = new byte[] { 0, 0, 0, 0, 
                              0, 0, 0, 0, 
                              0, 0, 0, 0, 
                              0, 0, 0, 0 };

    byte[] SKey = new byte[16];
    for (int i = 0; i < 16; i++){
      SKey[i] = (byte) (i+1);
    }

    SecretKeySpec SecretKey = new SecretKeySpec(SKey, "AES");
    IvParameterSpec cipherIV = new IvParameterSpec(iv);
    Cipher text = Cipher.getInstance("AES/CBC/ISO10126Padding");
    
    text.init(Cipher.DECRYPT_MODE, SecretKey, cipherIV);
    cipherBMP = text.update(cipherBMP);
    
    byte[] plainBMP = cipherBMP;    
    // END SOLUTION
    
    Files.write(Paths.get("plain1.bmp"), plainBMP);
  }

  static void P2() throws Exception {
    byte[] cipher = Files.readAllBytes(Paths.get("cipher2.bin"));
    // BEGIN SOLUTION
    byte[] iv = new byte[] { 0, 0, 0, 0, 
                             0, 0, 0, 0, 
                             0, 0, 0, 0, 
                             0, 0, 0, 0 };
      
    byte[] SKey = new byte[16];
    for (int i = 0; i < 16; i++){
      SKey[i] = (byte) (i+1);
    }
    SecretKeySpec SecretKey = new SecretKeySpec(SKey, "AES");
    IvParameterSpec cipherIV = new IvParameterSpec(iv);
    Cipher text = Cipher.getInstance("AES/CBC/NoPadding");
   
    byte[] modifiedCipher = new byte[48];

    for (int i = 0; i < 48; i++){
      if(i < 16){
        modifiedCipher[i] = cipher[32+i];
      }
      else if (i > 15 && i < 32){
        modifiedCipher[i] = cipher[i];
      }
      else {
        modifiedCipher[i] = cipher[i - 32];
      }
    }
    
    text.init(Cipher.DECRYPT_MODE, SecretKey, cipherIV);
    modifiedCipher = text.update(modifiedCipher);
    byte[] plain = modifiedCipher;
    // END SOLUTION
    
    Files.write(Paths.get("plain2.txt"), plain);
  }

  static void P3() throws Exception {
    byte[] cipherBMP = Files.readAllBytes(Paths.get("cipher3.bmp"));
    byte[] otherBMP = Files.readAllBytes(Paths.get("plain1.bmp"));
    
    // BEGIN SOLUTION
    byte[] modifiedBMP = cipherBMP;
    for(int i = 0; i < 3000; i++) {
      modifiedBMP[i] = otherBMP[i];
    }
    // END SOLUTION
    
    Files.write(Paths.get("cipher3_modified.bmp"), modifiedBMP);
  }

  static void P4() throws Exception {
    byte[] plainA = Files.readAllBytes(Paths.get("plain4A.txt"));
    byte[] cipherA = Files.readAllBytes(Paths.get("cipher4A.bin"));
    byte[] cipherB = Files.readAllBytes(Paths.get("cipher4B.bin"));
    
    // BEGIN SOLUTION
    byte[] plainB = cipherB;
    for(int i = 0; i < cipherB.length; i++){
      plainB[i] = (byte) ((plainA[i]) ^ (cipherA[i]) ^ (cipherB[i]));
    }
    
    // END SOLUTION
    
    Files.write(Paths.get("plain4B.txt"), plainB);
  }

  static void P5() throws Exception {
    byte[] cipherBMP = Files.readAllBytes(Paths.get("cipher5.bmp"));
    
    // BEGIN SOLUTION
    byte[] plainBMP = new byte[cipherBMP.length];
    byte[] otherBMP = Files.readAllBytes(Paths.get("plain1.bmp"));
    byte[] key = new byte[] {   0,   0,    0,   0, 
                                0,   0,    0,   0,
                                0,   0,    0,   0,
                                0,   0,    0,   0 }; // byte array size

    byte[] iv = new byte[16];
    byte[] copyValue = Arrays.copyOfRange(otherBMP, 0, 6);
    
    loop:
    for(int year = 0; year < 100; year++){
      key[0] = (byte)year;
      for(int month = 1; month < 13; month++){
        key[1] = (byte)month;
        for(int day = 1; day <= 31; day++){
          key[2] = (byte)day;

          SecretKeySpec SecretKey = new SecretKeySpec(key, "AES");
          IvParameterSpec CipherIV = new IvParameterSpec(iv);
          Cipher cipher = Cipher.getInstance("AES/CBC/ISO10126Padding");

          cipher.init(Cipher.DECRYPT_MODE, SecretKey, CipherIV);
          try {
            plainBMP = cipher.doFinal(cipherBMP);
            if(Arrays.equals(Arrays.copyOfRange(plainBMP, 0,6), copyValue)) {
              break loop;
            }
          }  // decryption might throw a BadPaddingException!
          catch (BadPaddingException e) {
          }
        }
      }
    }
    // END SOLUTION
    
    Files.write(Paths.get("plain5.bmp"), plainBMP);
  }

  public static void main(String [] args) {
    try {  
      P1();
      P2();
      P3();
      P4();
      P5();
    } catch (Exception e) {
      e.printStackTrace();
    } 
  }
}