#
# PySNMP MIB module GENERICOBJECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/GENERICOBJECT-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 16:24:54 2022
# On host fv-az126-328 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
cardGeneric, = mibBuilder.importSymbols("BASIS-MIB", "cardGeneric")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, iso, TimeTicks, Counter32, Counter64, Gauge32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "TimeTicks", "Counter32", "Counter64", "Gauge32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "Bits", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
genericObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 2, 8))
genericLineNum = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 8, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: genericLineNum.setStatus('mandatory')
if mibBuilder.loadTexts: genericLineNum.setDescription('This is the generic line number used in traps. This object\n         cannot be set or read. This object may refer to a T1, T3 \n         or X21 line. (It is a proxy for other objects lineNum,\n         dsx3LineNum and x21LineNum).\n\n         Currently, the ranges are\n         T1/E1    1..56\n         T3/E3    1..3\n         X21      1..4\n        ')
genericLineType = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 8, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 51, 52, 53, 54, 55, 56, 101, 102, 151, 152, 153, 154))).clone(namedValues=NamedValues(("dsx1ESF", 1), ("dsx1D4", 2), ("dsx1E1", 3), ("dsx1E1CRC", 4), ("dsx1E1MF", 5), ("dsx1E1CRC-MF", 6), ("dsx1E1clearchannel", 7), ("dsx3CbitParity", 51), ("dsx3g832-g804", 52), ("dsx3m13mode", 53), ("dsx3g751", 54), ("dsx3Unframed", 55), ("e3Unframed", 56), ("x21dte", 101), ("x21dce", 102), ("sonetSts3c", 151), ("sonetStm1", 152), ("sonetSts12c", 153), ("sonetStm4", 154)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: genericLineType.setStatus('mandatory')
if mibBuilder.loadTexts: genericLineType.setDescription('This is the generic line type used in traps. This object\n         cannot be set or read. Depending on the value, this object\n         may refer to a T1, T3 or X21 line type.\n\n         It is a proxy for other objects lineType, dsx3LineType and\n         x21LineType.\n        ')
genericTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 8, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: genericTimeStamp.setStatus('mandatory')
if mibBuilder.loadTexts: genericTimeStamp.setDescription('This is the generic time stamp used in traps. This object\n         cannot be set or read. This object will be used by all new\n         traps to tell the time that a given trap was originated.\n        ')
mibBuilder.exportSymbols("GENERICOBJECT-MIB", genericLineNum=genericLineNum, genericLineType=genericLineType, genericObjects=genericObjects, genericTimeStamp=genericTimeStamp)
