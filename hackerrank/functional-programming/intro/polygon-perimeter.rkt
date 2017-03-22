#lang racket

;; Given the cartesian coordinates of a set of points in a  plane. When
;; traversed sequentially, these points form a polygon which is not
;; self-intersecting in nature. Compute perimeter of polygon

(define (read-list)
  (let ([lst (read-line)])
    (map string->number (string-split lst))))

(define (read-points n)
  (cond [(= n 0) empty]
        [else (cons (read-list) (read-points (- n 1)))]))  

(define (euclid-dist p1 p2)
  (sqrt (+ (expt (- (list-ref p1 0) (list-ref p2 0)) 2)
           (expt (- (list-ref p1 1) (list-ref p2 1)) 2))))

(define (perimeter-helper points i tot)
  (cond [(= i -1) tot]
        [(= i 0)
         (+ (euclid-dist
             (list-ref points i)
             (list-ref points (- (length points) 1)))
            (perimeter-helper points (- i 1) tot))]
        [else
         (+ (euclid-dist
             (list-ref points i)
             (list-ref points (- i 1)))
            (perimeter-helper points (- i 1) tot))]))

(define (perimeter points)
  (perimeter-helper points (- (length points) 1) 0))

(define n (string->number (read-line)))
(define points (read-points n))
(display (perimeter points))

;; Unit Tests
(require rackunit)
(define epsilon 0.0001)
(check-eq? (perimeter (list (list 0 0) (list 1 0) (list 1 1) (list 0 1))) 4)
(check-true (< (- (perimeter (list (list 1043 770) (list 551 990) (list 681 463))) 
                  1556.3949033) 
               epsilon))
