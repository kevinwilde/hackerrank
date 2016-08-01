#lang racket

(define (zip l1 l2)
  (map list l1 l2))

(define l1 (string->list (read-line)))
(define l2 (string->list (read-line)))
(printf "~a" (list->string (flatten (zip l1 l2))))
