#
# PySNMP MIB module GENERICOBJECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/GENERICOBJECT-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 00:05:00 2022
# On host fv-az77-763 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
cardGeneric, = mibBuilder.importSymbols("BASIS-MIB", "cardGeneric")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, ModuleIdentity, Unsigned32, iso, IpAddress, Bits, Integer32, TimeTicks, NotificationType, Gauge32, ObjectIdentity, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "Unsigned32", "iso", "IpAddress", "Bits", "Integer32", "TimeTicks", "NotificationType", "Gauge32", "ObjectIdentity", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
genericObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 2, 8))
genericLineNum = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 8, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: genericLineNum.setStatus('mandatory')
genericLineType = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 8, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 51, 52, 53, 54, 55, 56, 101, 102, 151, 152, 153, 154))).clone(namedValues=NamedValues(("dsx1ESF", 1), ("dsx1D4", 2), ("dsx1E1", 3), ("dsx1E1CRC", 4), ("dsx1E1MF", 5), ("dsx1E1CRC-MF", 6), ("dsx1E1clearchannel", 7), ("dsx3CbitParity", 51), ("dsx3g832-g804", 52), ("dsx3m13mode", 53), ("dsx3g751", 54), ("dsx3Unframed", 55), ("e3Unframed", 56), ("x21dte", 101), ("x21dce", 102), ("sonetSts3c", 151), ("sonetStm1", 152), ("sonetSts12c", 153), ("sonetStm4", 154)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: genericLineType.setStatus('mandatory')
genericTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 8, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: genericTimeStamp.setStatus('mandatory')
mibBuilder.exportSymbols("GENERICOBJECT-MIB", genericLineType=genericLineType, genericObjects=genericObjects, genericLineNum=genericLineNum, genericTimeStamp=genericTimeStamp)
