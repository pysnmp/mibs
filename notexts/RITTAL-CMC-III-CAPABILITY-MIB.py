#
# PySNMP MIB module RITTAL-CMC-III-CAPABILITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/rittal/RITTAL-CMC-III-CAPABILITY-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:27:45 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
cmcIII, = mibBuilder.importSymbols("RITTAL-CMC-III-MIB", "cmcIII")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
NotificationType, Gauge32, Unsigned32, ModuleIdentity, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, TimeTicks, Integer32, IpAddress, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "Unsigned32", "ModuleIdentity", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "TimeTicks", "Integer32", "IpAddress", "Counter32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cmcIIICapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 2606, 7, 8))
cmcIIICapability.setRevisions(('2015-10-27 00:00', '2014-10-06 00:00', '2013-03-30 00:00', '2012-08-30 00:00', '2011-09-01 00:00',))
if mibBuilder.loadTexts: cmcIIICapability.setLastUpdated('201510270000Z')
if mibBuilder.loadTexts: cmcIIICapability.setOrganization('RITTAL GmbH & Co. KG')
cmcIIIPuCapsV102 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2606, 7, 8, 30102))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmcIIIPuCapsV102 = cmcIIIPuCapsV102.setProductRelease('V1.02')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmcIIIPuCapsV102 = cmcIIIPuCapsV102.setStatus('current')
cmcIIIPuCapsV103 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2606, 7, 8, 30103))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmcIIIPuCapsV103 = cmcIIIPuCapsV103.setProductRelease('V1.03')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmcIIIPuCapsV103 = cmcIIIPuCapsV103.setStatus('current')
cmcIIIPuCapsV104 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2606, 7, 8, 30104))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmcIIIPuCapsV104 = cmcIIIPuCapsV104.setProductRelease('V1.04')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmcIIIPuCapsV104 = cmcIIIPuCapsV104.setStatus('current')
cmcIIIPduCapsV104 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2606, 7, 8, 34104))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmcIIIPduCapsV104 = cmcIIIPduCapsV104.setProductRelease('V1.04')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmcIIIPduCapsV104 = cmcIIIPduCapsV104.setStatus('current')
mibBuilder.exportSymbols("RITTAL-CMC-III-CAPABILITY-MIB", cmcIIIPuCapsV102=cmcIIIPuCapsV102, cmcIIIPuCapsV103=cmcIIIPuCapsV103, PYSNMP_MODULE_ID=cmcIIICapability, cmcIIICapability=cmcIIICapability, cmcIIIPuCapsV104=cmcIIIPuCapsV104, cmcIIIPduCapsV104=cmcIIIPduCapsV104)
