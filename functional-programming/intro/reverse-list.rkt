#lang racket

(define (read-list)
  (let ([x (read)]) 
    (if (eof-object? x)
        (list)
        (cons x (read-list)))))

(define lst (read-list))

(define (print-list lst)
  (cond [(not (empty? lst)) (begin (printf "~s\n" (first lst))
                                   (print-list (rest lst)))]))

(define (reverse-list lst)
  (cond [(empty? lst) lst]
        [else (cons (last lst) (reverse-list (drop-right lst 1)))]))

; (print-list (reverse lst))  ; using built in reverse function
(print-list (reverse-list lst))  ; using my own reverse-list function