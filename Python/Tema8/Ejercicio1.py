def main():
    
    f = open('archivo.txt', 'w')
    f.write("dato1\n")
    f.close()

    f = open('archivo.txt', 'a')
    f.write("dato2\n")
    f.close()

if __name__ == '__main__':
    main()