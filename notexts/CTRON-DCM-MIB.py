#
# PySNMP MIB module CTRON-DCM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-DCM-MIB
# Produced by pysmi-1.1.12 at Wed Jul  3 12:22:24 2024
# On host fv-az1022-995 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ctDcm, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctDcm")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, IpAddress, MibIdentifier, Integer32, Gauge32, iso, ObjectIdentity, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "IpAddress", "MibIdentifier", "Integer32", "Gauge32", "iso", "ObjectIdentity", "Counter64", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dCM = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 6, 1))
dCMMode = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 6, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dCMMode.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-DCM-MIB", dCMMode=dCMMode, dCM=dCM)
