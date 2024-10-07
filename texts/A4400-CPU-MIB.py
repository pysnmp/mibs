#
# PySNMP MIB module A4400-CPU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/alcatel/A4400-CPU-MIB
# Produced by pysmi-1.1.12 at Mon Oct  7 02:49:36 2024
# On host fv-az775-99 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, IpAddress, MibIdentifier, Gauge32, ObjectIdentity, ModuleIdentity, Counter64, Unsigned32, Counter32, Integer32, NotificationType, iso, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "MibIdentifier", "Gauge32", "ObjectIdentity", "ModuleIdentity", "Counter64", "Unsigned32", "Counter32", "Integer32", "NotificationType", "iso", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
alcatel = MibIdentifier((1, 3, 6, 1, 4, 1, 637))
abs = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64))
a4400 = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 4400))
a4400CPU = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1))
pbxAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 1))
linux = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 1, 10))
unknown = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 1, 255))
pbxMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 0), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbxMibVersion.setStatus('mandatory')
if mibBuilder.loadTexts: pbxMibVersion.setDescription('The PBX MIB Version.')
pbxState = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("indeterminate", 0), ("critical", 1), ("major", 2), ("minor", 3), ("warning", 4), ("normal", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbxState.setStatus('mandatory')
if mibBuilder.loadTexts: pbxState.setDescription('The PBX state as defined by the trap manager.')
mibBuilder.exportSymbols("A4400-CPU-MIB", pbxMibVersion=pbxMibVersion, pbxAgent=pbxAgent, linux=linux, a4400=a4400, alcatel=alcatel, abs=abs, a4400CPU=a4400CPU, pbxState=pbxState, unknown=unknown)
