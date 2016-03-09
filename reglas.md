Pasos de compilación y salidas en la terminal:

1. Compilar ambos archivos como objetos separados
wtpc-15@ws2:~/Documentos/workshop/HOpython-compiled/src$ gcc -c add_two.c  -o add_two.o
wtpc-15@ws2:~/Documentos/workshop/HOpython-compiled/src$ gcc -c arrays.c -o arrays.o

2. Construir una librería dinámica que tenga ambos objetos
wtpc-15@ws2:~/Documentos/workshop/HOpython-compiled/src$ gcc -c -fPIC arrays.c
wtpc-15@ws2:~/Documentos/workshop/HOpython-compiled/src$ gcc -c -fPIC add_two.c
wtpc-15@ws2:~/Documentos/workshop/HOpython-compiled/src$ gcc -shared arrays.o add_two.o -o libMiLibreria.so

wtpc-15@ws2:~/Documentos/workshop/HOpython-compiled/src$ nm -n libMiLibreria.so
                 w __cxa_finalize@@GLIBC_2.2.5
                 w __gmon_start__
                 w _ITM_deregisterTMCloneTable
                 w _ITM_registerTMCloneTable
                 w _Jv_RegisterClasses
0000000000000610 T _init
0000000000000660 t deregister_tm_clones
0000000000000690 t register_tm_clones
00000000000006d0 t __do_global_dtors_aux
0000000000000710 t frame_dummy
0000000000000745 T add_int_array
00000000000007ba T dot_product
0000000000000836 T add_float
0000000000000860 T add_int
0000000000000874 T add_float_ref
00000000000008a7 T add_int_ref
00000000000008d4 T _fini
0000000000000a28 r __FRAME_END__
0000000000200e00 t __frame_dummy_init_array_entry
0000000000200e08 t __do_global_dtors_aux_fini_array_entry
0000000000200e10 d __JCR_END__
0000000000200e10 d __JCR_LIST__
0000000000200e18 d _DYNAMIC
0000000000201000 d _GLOBAL_OFFSET_TABLE_
0000000000201028 d __dso_handle
0000000000201030 B __bss_start
0000000000201030 b completed.6973
0000000000201030 D _edata
0000000000201030 d __TMC_END__
0000000000201038 B _end

Están como texto todas las funciones de los .c! :)

3. Escribir un script en python que pruebe **todas** las funciones
de la librería

ver main.py
