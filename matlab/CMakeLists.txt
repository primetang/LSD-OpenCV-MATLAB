PROJECT(MATLSD)

FIND_PACKAGE(OpenCV REQUIRED)

SET(OpenCV_INCLUDE_DIR1 $ENV{OpenCV_DIR}/include)
SET(OpenCV_INCLUDE_DIR2 $ENV{OpenCV_DIR}/include/opencv)

SET(MEX_NAME_SET
    lsd
    lsd_image
)

IF(WIN32)
    FIND_PROGRAM(MEX_CMD mex.bat)
    FIND_PROGRAM(MEXEXT_CMD mexext.bat)
ELSE()
    FIND_PROGRAM(MEX_CMD mex)
    FIND_PROGRAM(MEXEXT_CMD mexext)
ENDIF()

IF(MEX_CMD AND MEXEXT_CMD)

    GET_FILENAME_COMPONENT(MEX_REAL_CMD ${MEX_CMD} ABSOLUTE)
    GET_FILENAME_COMPONENT(MEX_PATH ${MEX_REAL_CMD} PATH)

    GET_FILENAME_COMPONENT(MEXEXT_REAL_CMD ${MEXEXT_CMD} ABSOLUTE)
    GET_FILENAME_COMPONENT(MEXEXT_PATH ${MEXEXT_REAL_CMD} PATH)

    IF(MEX_PATH STREQUAL MEXEXT_PATH)
        MESSAGE(STATUS "Found MATLAB at: " ${MEX_PATH})

        EXECUTE_PROCESS(COMMAND ${MEXEXT_REAL_CMD} OUTPUT_VARIABLE MEX_EXTENSION OUTPUT_STRIP_TRAILING_WHITESPACE)

        FOREACH(MEX_NAME ${MEX_NAME_SET})

            SET(MEX_FILE ${MATLSD_BINARY_DIR}/${MEX_NAME}.${MEX_EXTENSION})

            ADD_CUSTOM_COMMAND(
                OUTPUT ${MEX_FILE}
                COMMAND ${MEX_REAL_CMD}
                ARGS ${MATLSD_SOURCE_DIR}/${MEX_NAME}.cpp -I${LSD_SOURCE_DIR}/include -I${OpenCV_INCLUDE_DIR1} -I${OpenCV_INCLUDE_DIR2} -L${LIBRARY_OUTPUT_PATH} -L${OpenCV_LIB_PATH} -llsd -lopencv_core247 -lopencv_highgui247 -lopencv_imgproc247
                COMMENT "Building MEX extension ${MEX_FILE}"
            )
            ADD_CUSTOM_TARGET(mex_${MEX_NAME} ALL DEPENDS ${MEX_FILE})
        ENDFOREACH(MEX_NAME)
    ELSE()
        MESSAGE(SEND_ERROR
            "The 'mex' and 'mexext' programs have been found in different locations. It's likely that one of them is not part of the MATLAB instalation. Make sure that the 'bin' directory from the MATLAB instalation is in PATH"
        )
    ENDIF()
ELSE()
    MESSAGE(SEND_ERROR
        "Cannot find MATLAB or Octave instalation. Make sure that the 'bin' directory from the MATLAB instalation or that mkoctfile is in PATH"
    )
ENDIF()