#
# PySNMP MIB module CTRON-DCM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-DCM-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 10:06:01 2024
# On host fv-az575-513 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ctDcm, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctDcm")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ModuleIdentity, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, IpAddress, Integer32, Unsigned32, TimeTicks, iso, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "IpAddress", "Integer32", "Unsigned32", "TimeTicks", "iso", "Bits", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dCM = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 6, 1))
dCMMode = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 6, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dCMMode.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-DCM-MIB", dCM=dCM, dCMMode=dCMMode)
