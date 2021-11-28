#
# PySNMP MIB module A4400-CPU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/alcatel/A4400-CPU-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 16:33:53 2021
# On host fv-az126-355 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, ModuleIdentity, Integer32, MibIdentifier, NotificationType, Unsigned32, IpAddress, Counter64, ObjectIdentity, enterprises, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "ModuleIdentity", "Integer32", "MibIdentifier", "NotificationType", "Unsigned32", "IpAddress", "Counter64", "ObjectIdentity", "enterprises", "Bits", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alcatel = MibIdentifier((1, 3, 6, 1, 4, 1, 637))
abs = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64))
a4400 = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 4400))
a4400CPU = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1))
pbxAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 1))
linux = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 1, 10))
unknown = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 1, 255))
pbxMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 0), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbxMibVersion.setStatus('mandatory')
pbxState = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("indeterminate", 0), ("critical", 1), ("major", 2), ("minor", 3), ("warning", 4), ("normal", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbxState.setStatus('mandatory')
mibBuilder.exportSymbols("A4400-CPU-MIB", unknown=unknown, pbxMibVersion=pbxMibVersion, alcatel=alcatel, abs=abs, a4400=a4400, pbxAgent=pbxAgent, pbxState=pbxState, linux=linux, a4400CPU=a4400CPU)
