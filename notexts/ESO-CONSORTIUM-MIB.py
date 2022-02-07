#
# PySNMP MIB module ESO-CONSORTIUM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/eso/ESO-CONSORTIUM-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:12:09 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Counter32, Counter64, TimeTicks, enterprises, Gauge32, MibIdentifier, NotificationType, Bits, Integer32, ModuleIdentity, ObjectIdentity, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, snmpModules = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "Counter64", "TimeTicks", "enterprises", "Gauge32", "MibIdentifier", "NotificationType", "Bits", "Integer32", "ModuleIdentity", "ObjectIdentity", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "snmpModules")
DisplayString, AutonomousType, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "AutonomousType", "TextualConvention")
esoConsortiumMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14832))
esoConsortiumMIB.setRevisions(('2004-06-23 00:00', '2003-02-03 00:00', '2003-02-03 00:00',))
if mibBuilder.loadTexts: esoConsortiumMIB.setLastUpdated('200406230000Z')
if mibBuilder.loadTexts: esoConsortiumMIB.setOrganization('ESO (Extended Security Options) Consortium')
esoConsortiumMIBObjectIdentities = MibIdentifier((1, 3, 6, 1, 4, 1, 14832, 1))
usm3DESPrivProtocol = ObjectIdentity((1, 3, 6, 1, 4, 1, 14832, 1, 1))
if mibBuilder.loadTexts: usm3DESPrivProtocol.setStatus('current')
usmAESCfb128PrivProtocol = ObjectIdentity((1, 3, 6, 1, 4, 1, 14832, 1, 2))
if mibBuilder.loadTexts: usmAESCfb128PrivProtocol.setStatus('deprecated')
usmAESCfb192PrivProtocol = ObjectIdentity((1, 3, 6, 1, 4, 1, 14832, 1, 3))
if mibBuilder.loadTexts: usmAESCfb192PrivProtocol.setStatus('current')
usmAESCfb256PrivProtocol = ObjectIdentity((1, 3, 6, 1, 4, 1, 14832, 1, 4))
if mibBuilder.loadTexts: usmAESCfb256PrivProtocol.setStatus('current')
mibBuilder.exportSymbols("ESO-CONSORTIUM-MIB", usmAESCfb256PrivProtocol=usmAESCfb256PrivProtocol, esoConsortiumMIBObjectIdentities=esoConsortiumMIBObjectIdentities, esoConsortiumMIB=esoConsortiumMIB, usm3DESPrivProtocol=usm3DESPrivProtocol, usmAESCfb192PrivProtocol=usmAESCfb192PrivProtocol, usmAESCfb128PrivProtocol=usmAESCfb128PrivProtocol, PYSNMP_MODULE_ID=esoConsortiumMIB)
